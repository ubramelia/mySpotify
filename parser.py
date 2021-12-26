import json

f = open("userIDplaylist.json")
data = json.load(f)

for i in data['items']:
    print(i['name'])
    print(i['owner']['display_name'])
    print(i['owner']['external_urls']['spotify'])
    print(i['id'])
    print()
