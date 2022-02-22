import requests
import json

resp = requests.get('https://www.googleapis.com/youtube/v3/search')

print(resp.status_code)
print(resp.body)
