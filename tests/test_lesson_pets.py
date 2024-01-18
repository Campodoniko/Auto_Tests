import requests
import pytest

# Pet Tests
def test_get_pet():
    response = requests.get('https://petstore.swagger.io/v2/pet/1')
    assert response.status_code == 200

def test_create_pet():
    pet_data = {"id": 0, "category": {"id": 0, "name": "string"}, "name": "doggie",
                "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}], "status": "available"}
    response = requests.post('https://petstore.swagger.io/v2/pet', json=pet_data)
    assert response.status_code == 200

def test_update_pet():
    pet_data = {"id": 0, "category": {"id": 0, "name": "string"}, "name": "doggie",
                "photoUrls": ["string"], "tags": [{"id": 0, "name": "string"}], "status": "sold"}
    response = requests.put('https://petstore.swagger.io/v2/pet', json=pet_data)
    assert response.status_code == 200

def test_delete_pet():
    response = requests.delete('https://petstore.swagger.io/v2/pet/0')
    assert response.status_code == 200

def test_find_by_status_pet():
    params = {'status': 'available'}
    response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params)
    assert response.status_code == 200

# Store Tests
def test_get_inventory():
    response = requests.get('https://petstore.swagger.io/v2/store/inventory')
    assert response.status_code == 200

def test_order_pet():
    order_data = {"id": 0, "petId": 0, "quantity": 0, "shipDate": "2022-12-30T16:32:16Z",
                  "status": "placed", "complete": False}
    response = requests.post('https://petstore.swagger.io/v2/store/order', json=order_data)
    assert response.status_code == 200

def test_get_order():
    response = requests.get('https://petstore.swagger.io/v2/store/order/0')
    assert response.status_code == 200

def test_delete_order():
    response = requests.delete('https://petstore.swagger.io/v2/store/order/0')
    assert response.status_code == 200

# User Tests
def test_create_user():
    user_data = {"id": 0, "username": "user1", "firstName": "Firstname", "lastName": "Lastname",
                 "email": "email@mail.com", "password": "password", "phone": "12345678", "userStatus": 0}
    response = requests.post('https://petstore.swagger.io/v2/user', json=user_data)
    assert response.status_code == 200

def test_get_user():
    response = requests.get('https://petstore.swagger.io/v2/user/user1')
    assert response.status_code == 200

def test_update_user():
    user_data = {"id": 0, "username": "user1", "firstName": "UpdatedName", "lastName": "UpdatedLastname",
                 "email": "newemail@mail.com", "password": "newpassword", "phone": "87654321", "userStatus": 0}
    response = requests.put('https://petstore.swagger.io/v2/user/user1', json=user_data)
    assert response.status_code == 200

def test_delete_user():
    response = requests.delete('https://petstore.swagger.io/v2/user/user1')
    assert response.status_code == 200

def test_login_user():
    params = {'username': 'user1', 'password': 'password'}
    response = requests.get('https://petstore.swagger.io/v2/user/login', params=params)
    assert response.status_code == 200

def test_logout_user():
    response = requests.get('https://petstore.swagger.io/v2/user/logout')
    assert response.status_code == 200