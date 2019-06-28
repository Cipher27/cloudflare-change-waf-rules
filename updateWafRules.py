import requests
import json
import os

ZONE_ID = os.environ.get("CF_ZONE_ID") 
HEADERS = {"X-Auth-Email": os.environ.get("CF_AUTH_EMAIL"), "X-Auth-Key": os.environ.get("CF_AUTH_KEY"), "Content-Type": "application/json"}
CLOUDFLARE_PACKAGE_NAME = "CloudFlare"

r = requests.get(url = "https://api.cloudflare.com/client/v4/zones/" + ZONE_ID + "/firewall/waf/packages", headers = HEADERS) 
waf_packages = r.json()

for package in waf_packages['result']:
	if (package['name'] == CLOUDFLARE_PACKAGE_NAME):
		r = requests.get(url = "https://api.cloudflare.com/client/v4/zones/" + ZONE_ID + "/firewall/waf/packages/" + package['id'] + "/groups", headers = HEADERS)
		rule_groups = r.json()
		for group in rule_groups['result']:
			if group['mode'] == "on":
				r = requests.request("GET", "https://api.cloudflare.com/client/v4/zones/" + ZONE_ID + "/firewall/waf/packages/" + group['package_id'] + "/rules?group_id=" + group['id'], headers = HEADERS)
				rules = r.json()
				for page in range(1, int(rules['result_info']['total_pages']) + 1):
					r = requests.request("GET", "https://api.cloudflare.com/client/v4/zones/" + ZONE_ID + "/firewall/waf/packages/" + group['package_id'] + "/rules?page=" + str(page), headers = HEADERS)
					rules = r.json()
					for rule in rules['result']:
						DATA = {}
						DATA['mode'] = 'simulate'
						r = requests.request("PATCH", "https://api.cloudflare.com/client/v4/zones/" + ZONE_ID + "/firewall/waf/packages/" + group['package_id'] + "/rules/" + rule['id'], data = json.dumps(DATA), headers = HEADERS)
						print (r.json())