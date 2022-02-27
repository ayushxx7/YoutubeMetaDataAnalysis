import requests
import json


def set_api_key():
    """Set the API key to use for the YouTube Data API.

    Parameters
    ----------
    None

    Returns
    -------
    str:
        The API key to use for the YouTube Data API.
    """
    with open('creds.json') as f:
        creds = json.load(f)
    api_key = creds["api_key"]

    return api_key


def get_search_results_data(api_key, query='python'):
    """Get the search results data from the YouTube Data API.

    Parameters
    ----------
    api_key: str
        The API key to use for the YouTube Data API.

    Returns
    -------
    dict:
        The search results data from the YouTube Data API.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    search = 'https://www.googleapis.com/youtube/v3/search'

    params = {
        'q': query,
        'key': api_key,
        'maxResults': 50,
    }

    data = {}
    items = []

    vid_count = 50

    while vid_count < 400:
        print(f'fetching data. vid_count {vid_count}')
        resp = requests.get(search, params=params)

        if 'nextPageToken' in resp.json():
            next_page_token = resp.json()['nextPageToken']
            params['pageToken'] = next_page_token

        items.extend(resp.json()["items"])
        data.update(resp.json())

        vid_count += 50

    data['items'] = items

    return data


def write_data_to_json(data, file_name='search_results.json'):
    """Write the results data to a file.

    Parameters
    ----------
    data: dict
        The search results data from the YouTube Data API.
    file_name: str
        The name of the file to write the data to.

    Returns
    -------
    None
    """
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=2)


def read_json_data(file_name):
    """Read the data from a file.

    Parameters
    ----------
    file_name: str
        The name of the file to read the data from.

    Returns
    -------
    dict:
        The data from the file.
    """
    with open(file_name, 'r') as f:
        data = json.load(f)

    return data


def get_video_metadata(api_key, list_of_videos):
    """Get the video metadata from the YouTube Data API.

    Parameters
    ----------
    api_key: str
        The API key to use for the YouTube Data API.
    list_of_videos: list
        The list of videos to get the metadata for.

    Returns
    -------
    dict:
        The video metadata from the YouTube Data API.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    videos_base_url = 'https://www.googleapis.com/youtube/v3/videos'
    part = 'snippet,statistics,topicDetails,contentDetails'
    id = ','.join(list_of_videos)

    metadata_url = f'{videos_base_url}?part={part}&id={id}&key={api_key}'
    resp = requests.get(metadata_url, headers=headers)
    data = resp.json()

    return data

def keep_video_results(data):
    """Keep only the video results from the data.

    Parameters
    ----------
    data: dict
        The search results data from the YouTube Data API.

    Returns
    -------
    list:
        The video results from the data.
    """
    items = data['items']
    video_ids = set()

    for item in items:
        if item['id']['kind'] == 'youtube#video':
            video_ids.add(item['id']['videoId'])

    return video_ids

def keep_relevant_data(data):
    """Keep only the relevant data from the data.

    Parameters
    ----------
    data: dict
        The search results data from the YouTube Data API.

    Returns
    -------
    list:
        The relevant data from the data.
    """
    video_data = {}

    for index, key in enumerate(data["items"]):
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
            # it's fine if we loose a couple of data points
            # if they don't have the relevant data such as tags.
            pass

    return video_data

if __name__ == '__main__':
    api_key = set_api_key()
    youtube_search_data = get_search_results_data(api_key)
    write_data_to_json(youtube_search_data, 'search_results.json')
    video_ids = keep_video_results(youtube_search_data)
    write_data_to_json(video_ids, 'video_ids.json')
    video_metadata = get_video_metadata(api_key, video_ids)
    write_data_to_json(video_metadata, 'video_metadata.json')
    relevant_data = keep_relevant_data(video_metadata)
    write_data_to_json(relevant_data, 'video_relevant_data.json')
