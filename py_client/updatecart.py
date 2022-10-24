import requests

endpoint = 'http://127.0.0.1:8000/api/carts/2/'
json = {
    'is_ordered': False
}
response = requests.put(endpoint, json=json)
print(response.json())