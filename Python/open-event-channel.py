import json, requests, sseclient, pprint

# SSE Client Setup
url = "<Your_URL>"

def with_requests(url):
    return requests.get(url, stream = True, verify = False)

response = with_requests(url)
client = sseclient.SSEClient(response)
for event in client.events():
    pprint.pprint(json.loads(event.data))
