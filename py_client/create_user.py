from getpass import getpass
import requests

email = input('Email: ')
password = getpass('Password: ')
password1 = getpass('Confirm password: ')

data = {
    'email': email,
    'password': password,
    'password1': password1
}

resp = requests.post('http://127.0.0.1:8000/api/signup/', json=data)
print(resp.json())

