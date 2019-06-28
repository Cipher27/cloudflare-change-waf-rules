# CloudFlare Change Waf Rule Actions

This project is meant to help you avoid the pesky task of turning the 350+ cloudflare rules to simulate in your WAF, in order to build a baseline of potential false positives your application may trigger.

## Getting Started

Clone the repo to your local machine, define the 3 required environment variables, and off you go!

### Prerequisites

You may need to install the python requests library, or possibly update some dependencies.

python2.7
```
pip install requests
```

python3
```
pip3 install requests
```

Define your relevant environment variables.

```
export CF_ZONE_ID=
export CF_AUTH_EMAIL=
export CF_AUTH_KEY=
```

Run it!

```
python3 updateWafRules.py
```

## Running the tests

Go check your CloudFlare rules in the UI, they will be set to simulate. Or watch the output of the requests while the script is running.

## Authors

* **Conor Murray**

## License

Use it for whatever