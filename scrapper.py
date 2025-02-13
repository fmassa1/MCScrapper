import requests
import re
import json

newest_videos = []

def extract_video_titles(html):
    matches = re.findall(r'"title":\{"runs":\[\{"text":"(.*?)"\}\]', html)
    return matches

def is_new_video(videos):
    if len(newest_videos) is 0:
        newest_videos.append[videos[2]]
        newest_videos.append[videos[1]]
        newest_videos.append[videos[0]]

    elif videos[0] not in newest_videos:
        newest_videos.pop(0)
        newest_videos.append(videos[0])


def retrieve_html(url):
    r = requests.get(url)
    return r.status_code, r.text




if __name__ == '__main__':
    

    while True:
        status, html = retrieve_html('https://youtube.com/user/penguinz0/videos')
        titles = extract_video_titles(html)
        print(titles[0])