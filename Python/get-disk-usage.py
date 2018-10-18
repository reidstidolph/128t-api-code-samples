import requests, json

# Retrive Stat (Session Count)

url = "<Your_URL>"
token = "<Your_Token>"
header = {'Authorization': 'Bearer {}'.format(token)}
payload = {} #leave this empty
response = requests.post(url, data = json.dumps(payload), headers = header, verify = False)
print(response.text)
