import json

with open('data.json', 'r') as f:
    data = json.load(f)

# print(data)

items = data['items']

type_of_ids = set()
video_ids = set()

for item in items:
    # print(item['id'])
    type_of_ids.add(item['id']['kind'])

    if item['id']['kind'] == 'youtube#video':
        video_ids.add(item['id']['videoId'])

print(type_of_ids)
print(len(video_ids))

with open('videos.json', 'w') as f:
    json.dump(list(video_ids), f)
