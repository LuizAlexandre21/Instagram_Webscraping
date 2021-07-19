import requests
import pandas as pd
import re
from urllib.parse import urlencode
from datetime import datetime
import json


# Função Proxies

url = requests.get('https://www.instagram.com/centrouniversitariofariasbrito/?__a=1',headers = {'User-agent': 'your bot 0.1'})


texto = url.json()

user_id = texto['graphql']['user']['id']
page = texto['graphql']['user']['full_name'].lower().replace(" ", "")
edges = texto['graphql']['user']['edge_owner_to_timeline_media']['edges']
post_page=[]
for j in edges:
    url = 'https://www.instagram.com/p/' + j['node']['shortcode']
    post_page.append(url)
    video = j['node']['is_video']
    post_id = j['node']['id']
    date_posted_timestamp = j['node']['taken_at_timestamp']
    date_posted_human = datetime.fromtimestamp(date_posted_timestamp).strftime("%Y-%m-%d %H:%M:%S")
    times = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "edge_media_preview_like" in j['node'].keys():
        like_count = j['node']['edge_media_preview_like']['count']
    else:
        ""
    if 'edge_media_to_comment' in j['node'].keys():
        comment_count = j['node']['edge_media_to_comment']['count']
    else:
        ""
    if video:
        image_url = j['node']['display_url']
    else:
        image_url = j['node']['thumbnail_resources'][-1]['src']

    item = { 'Rede_Social': 'Instagram', 'Post_URL': url, 'Data': date_posted_human,'Curtida': like_count, 'Comentário': comment_count, 'updated_at': times}
    print(item)



