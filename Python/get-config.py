import requests, json

# Retrieving Configuration

url = "<Your_URL>"
token = "<Your_Token>"
header = {'Authorization': 'Bearer {}'.format(token)}
response = requests.get(url, headers = header, verify = False)
print(response.text)
