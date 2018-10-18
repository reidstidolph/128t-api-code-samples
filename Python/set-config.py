import requests, json

# Modifying Configuration

url = "<Your_URL>"
token = "<Your_Token>"
header = {'Authorization': 'Bearer {}'.format(token)}
payload2 = {"<Your_Mod>": "<Your_Mod>"}
response = requests.patch(url, json = payload2, headers = header, verify = False)
print(response.text)
