#!/usr/bin/env python3

# This fetches an authentication token from a 128T host

# Import modules
import requests, json

# Disable warning thrown when requests are made to 128T using  self-signed cert.
# DO NOT USE IN PRODUCTION APP!
# Instead it is reccomended to use a trusted cert on your 128T, and omit this.
requests.packages.urllib3.disable_warnings()

# URL for retrieving token. Update with your host address or FQDN
url = "https://<128T-HOST>/api/v1/login"
# Request payload
requestPayload = {
  'username': '<Username>',
  'password': '<Password>'
}
# Request headers
requestHeaders = {'content-type': 'application/json'}

# Create token request
response = requests.post(
  url,
  data=json.dumps(requestPayload),
  headers = requestHeaders,
  # Do not verify that SSL certificate provided by 128T host is trusted
  # DO NOT USE IN PRODUCTION APP!
  # Instead it is reccomended to use a trusted cert on your 128T, and omit this
  verify = False
)

# Print results of token request
print(response.text)
