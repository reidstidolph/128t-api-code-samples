#!/usr/bin/env python3

# Import modules
import requests, json

# Disable warning thrown when requests are made to 128T hosts using default self-signed cert)
# DO NOT USE IN PRODUCTION APP!
# Instead it is reccomended to use a trusted cert on your 128T, and omit this line
requests.packages.urllib3.disable_warnings()

# Retrieving Authentication Token
# URL for retrieving token. Update with your host address or FQDN
url = "https://<your-128T-host>/api/v1/login"
payload = {
  'username': '<Username>',
  'password': '<Password>'
}
requestHeaders = {'content-type': 'application/json'}

# Create token request
response = requests.post(
  url,
  data=json.dumps(payload),
  headers = requestHeaders,
  # Do not verify that SSL certificate provided by 128T host is trusted
  # DO NOT USE IN PRODUCTION APP!
  # Instead it is reccomended to use a trusted cert on your 128T, and omit this line
  verify = False
)

# Print results of token request
print(response.text)
