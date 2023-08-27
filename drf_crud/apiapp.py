import requests
import json

# URL = "http://localhost:8000/" # Function Based url 
URL = "http://localhost:8000/stdclsapi/" # Classe Based url

def get_data(id=None):
    data = {}
    # data = {'id':10}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)
    data = r.json()
    print(data)
get_data()


# Create data
def post_data():
    data = {
        'name':'TestclassBased',
        'stdclass':'9',
        'roll':'153',
        'city':'Califonia'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
# post_data()


#Update data ===> put
def update_data():
    data = {
        'id':7,
        'name':'cls update',
        'stdclass':24,
        'city':'Natore'
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
# update_data()

# Delete data
def delete_data():
    data = {'id':8}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
# delete_data()
# get_data()

