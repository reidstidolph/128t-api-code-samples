#!/usr/bin/env python3

# This retrieves key performance metrics for a given router node.

# Import modules
import sys, requests, json

# Disable warning thrown when requests are made to 128T using self-signed cert.
# DO NOT USE IN PRODUCTION APP!
# Instead it is recommended to use a trusted cert on 128T, and omit this.
requests.packages.urllib3.disable_warnings()

# Valid auth token string
token = "<Your_Token_String>"
# URL for retrieving config. Update with your host address or FQDN
url = "https://<128T-HOST>/api/v1/router/<ROUTER-NAME>/node/<NODE-NAME>"
# Request headers
requestHeaders = {'Authorization': 'Bearer {}'.format(token)}

# Try request to 128T host
try:
  response = requests.get(
    url,
    headers = requestHeaders,
    # Do not verify that SSL certificate provided by 128T host is trusted
    # DO NOT USE IN PRODUCTION APP!
    # Instead it is recommended to use a trusted cert on 128T, and omit this
    verify = False
  )
# Handle errors connecting to 128T host
except requests.exceptions.RequestException as error:
  print(error)
  sys.exit(1)

# Handle success response from 128T host
if response.status_code == 200:
  # Parse response payload into JSON object
  responsePayload = json.loads(response.text)
  # Print results of node info request (using json.dumps for pretty formatting)
  print(json.dumps(responsePayload, sort_keys=False, indent=2))

# Handle error response from 128T host
else:
  print('Error code: ' + str(response.status_code))
  print(response.text)
  sys.exit(1)
