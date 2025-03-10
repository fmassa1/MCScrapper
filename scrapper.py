# import requests
# import re
# import json
# import time


# newest_videos = []

# def extract_video_titles(html):
#     matches = re.findall(r'"title":\{"runs":\[\{"text":"(.*?)"\}\]', html)
#     return matches

# def is_new_video(videos):
#     if len(newest_videos) == 0:
#         newest_videos.append(videos[2])
#         newest_videos.append(videos[1])
#         newest_videos.append(videos[0])

#     elif videos[0] not in newest_videos:
#         newest_videos.pop(0)
#         newest_videos.append(videos[0])
#         update_user


# def retrieve_html(url):
#     r = requests.get(url)
#     return r.status_code, r.text


# def update_user():
#     return


# if __name__ == '__main__':
    
#     while True:
#         status, html = retrieve_html('https://youtube.com/user/penguinz0/videos')
#         if status == 200:
#             titles = extract_video_titles(html)
#             is_new_video(titles)
#             print(newest_videos)
#         else:
#             print(f"Failed to retrieve page. Status code: {status}")
#         time.sleep(3600)

import googleapiclient.discovery
import requests
from key import key
# API information
api_service_name = "youtube"
api_version = "v3"
# API key
DEVELOPER_KEY = key
moistcritical_ID = "UCq6VFHwMzcMXbuKyG7SQYIg"
# API client

newest_videos = []

def get_newest_video(id):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    search_request = youtube.search().list(
        part="snippet",
        channelId="UCq6VFHwMzcMXbuKyG7SQYIg",
        maxResults=1,
        order="date",
        type="video"
    )

    search_response = search_request.execute()

    if search_response["items"]:
        video = search_response["items"][0]["snippet"]["title"]
        print(f"Latest Video: {video}")
        
        if video not in newest_videos:
            newest_videos.append(video)
            if len(newest_videos) > 3:
                newest_videos.pop()

    else:
        print("No videos found.")

    #print(search_response)
    print(newest_videos)

if __name__ == '__main__':
    
    get_newest_video(moistcritical_ID)