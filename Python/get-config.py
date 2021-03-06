#!/usr/bin/env python3

# This retrieves running configuration from a 128T host

# Import modules
import requests, json

# Disable warning thrown when requests are made to 128T using self-signed cert.
# DO NOT USE IN PRODUCTION APP!
# Instead it is reccomended to use a trusted cert on your 128T, and omit this.
requests.packages.urllib3.disable_warnings()

# Valid auth token string
token = "<Your_Token_String>"
# URL for retrieving config. Update with your host address or FQDN
url = "https://<128T-HOST>/api/v1/config/getJSON?source=running"
# Request headers
requestHeaders = {'Authorization': 'Bearer {}'.format(token)}

# Create config request
response = requests.get(
  url,
  headers = requestHeaders,
  # Do not verify that SSL certificate provided by 128T host is trusted
  # DO NOT USE IN PRODUCTION APP!
  # Instead it is reccomended to use a trusted cert on your 128T, and omit this
  verify = False
)

# Parse response payload into JSON object
responsePayload = json.loads(response.text)

# Print results of config request (using json.dumps for pretty formatting)
print(json.dumps(responsePayload, sort_keys=False, indent=2))
