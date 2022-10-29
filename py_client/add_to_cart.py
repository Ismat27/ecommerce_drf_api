import requests

headers = {
    'Authorization': 'Token 541c335d1a0d78079bd35aa9645b8e0362297a3d'
}

data = {
    'product_id': 2,
    'quantity': 4,
}

resp = requests.post('http://127.0.0.1:8000/api/carts/items/', json=data, headers=headers)
print(resp.json())

