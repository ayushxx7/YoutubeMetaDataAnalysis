import requests
import json

# get api_key from creds.json
with open('creds.json') as f:
    creds = json.load(f)
api_key = creds["api_key"]

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

vid_search = 'https://www.googleapis.com/youtube/v3/videos'

with open('videos.json', 'r') as f:
    videos = json.load(f)

video_data = {}

# for index, video_id in enumerate(videos):
#     print(f'processing {index} out of {len(videos)}')
#     print(f'processing {video_id}')
#     vid_url = vid_search + '?part=snippet,statistics,topicDetails,contentDetails&id=' + video_id + '&key=' + api_key
#     r = requests.get(vid_url, headers=headers)
#     vid_json = r.json()

#     print(vid_json)

#     video_data[video_id] = vid_json

#     break

print(", ".join(videos))

vid_url = vid_search + '?part=snippet,statistics,topicDetails,contentDetails&id=' + ",".join(videos) + '&key=' + api_key

print(vid_url)
r = requests.get(vid_url, headers=headers)
vid_json = r.json()


# print(vid_json)

with open('video_data.json', 'w') as f:
    json.dump(vid_json, f)
    # vid_title = vid_json['items'][0]['snippet']['title']
    # st.markdown(vid_title, unsafe_allow_html=True)
