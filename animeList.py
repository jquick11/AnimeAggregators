import requests 
import json 
import sqlite3
import os 
url = "https://animechan.vercel.app/api/quotes/anime?title=Bleach"
response = requests.get(url)
print(response.text)


# 1: got the url request information


# process the data and make sure each rank show up, its possible because there is same score ratings
url= 'https://api.jikan.moe/v4/top/anime?page={}'
anime_info = {}
for i in range(5):
    u = url.format(i)
    response = requests.get(u)
    val = response.json()
    search_result = val['data']
    for anime_data in search_result:
        anime_info[anime_data['rank']] = (anime_data['title'],anime_data['score'], anime_data['popularity'])
print(anime_info)

# store into sql databases 
limit = 25 
offset = 0 
def database_setup(anime_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+anime_name)
    cur = conn.cursor()
    return cur, conn 

def anime_list_table(cur, conn):
    cur.execute()