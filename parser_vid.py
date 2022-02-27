import json

with open('video_data.json') as f:
    data = json.load(f)

video_data = {}

for index, key in enumerate(data["items"]):
    print(key)

    try:
        video_data[key["id"]] = {
            "id": key["id"],
            "publishedAt": key["snippet"]["publishedAt"],
            "tags": key["snippet"]["tags"],
            "categoryId": key["snippet"]["categoryId"],
            "duration": key["contentDetails"]["duration"],
            "viewCount": key["statistics"]["viewCount"],
            "likeCount": key["statistics"]["likeCount"],
            "commentCount": key["statistics"]["commentCount"],
            "topicCategories": key["topicDetails"]["topicCategories"]
        }
    except:
        pass

with open("video_relevant_data.json", "w") as f:
    json.dump(video_data, f)

