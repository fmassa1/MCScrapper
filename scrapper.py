import requests
import re
import json

def extract_video_titles(html):
    matches = re.findall(r'"title":\{"runs":\[\{"text":"(.*?)"\}\]', html)
    return matches

def retrieve_html(url):
    r = requests.get(url)
    return r.status_code, r.text



if __name__ == '__main__':
    status, html = retrieve_html('https://youtube.com/user/penguinz0/videos')
    titles = extract_video_titles(html)
    print(titles)