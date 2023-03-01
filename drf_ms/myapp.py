import requests
import json

# Create new a student to api
def createPost():
    data = {
        'title':'test json singer1',
        'duration':'3.31',
        'singer':'1'
    }
    header = {"content-Type":"application/json"}
    json_data = json.dumps(data)
    r = requests.post(url="http://127.0.0.1:8000/api/song/",headers=header, data=json_data)
    data = r.json()
    print(json_data)
    print(data)
# createPost()

#  View all song
def getSongInfo():
    URL = 'http://127.0.0.1:8000/api/song/'
    r = requests.get(url=URL)
    print(r)
    data = r.json()
    print(f'View all Song >> {data}')
getSongInfo()

#  View all Singer
def getSingerInfo():
    URL = 'http://127.0.0.1:8000/api/singer/'
    r = requests.get(url=URL)
    print(r)
    data = r.json()
    print(f'View all Singer and song info >> {data}')
getSingerInfo()