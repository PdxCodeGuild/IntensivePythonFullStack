import pprint

import requests

# response = requests.get("https://developer.trimet.org/ws/v2/vehicles?appID=D065A3A5DAE4622752786CEB9&routes=70")
response = requests.get("https://developer.trimet.org/ws/v2/vehicles", params={'appID': 'D065A3A5DAE4622752786CEB9', 'routes': 70})

pprint.pprint(response.json())
print(response.url)
print(response.status_code) # 200
print(response.encoding) # ISO-8859-1
print(response.headers)