import random, requests, json, pprint, sseclient

# Retrieving Authentication Token

url = "<Your_URL>"
payload = {
    'username': '<Username>',
    'password': '<Password>'
}

header1 = {'content-type': 'application/json'}
response = requests.post(url, data=json.dumps(payload), headers = header1, verify = False)

print(response.text)
