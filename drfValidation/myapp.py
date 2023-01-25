import requests
import json

# Create new a student to api
data = {
    'name':'test',
    'roll':'1304',
    'city':'Dhaka'
}
json_data = json.dumps(data)
r = requests.post(url="http://127.0.0.1:8000/api/student-create/", data=json_data)
data = r.json()
print(json_data)
print(data)

#  View all students with from api
URL = 'http://127.0.0.1:8000/api/'
# r = requests.get(url="http://127.0.0.1:8000/students/")
r = requests.get(url=URL)
print(r)
data = r.json()
print(f'View all students >> {data}')

