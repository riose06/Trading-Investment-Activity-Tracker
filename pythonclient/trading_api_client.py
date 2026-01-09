import requests

BASE_URL = "http://localhost:8080"  # your API base URL

def register_user(username, password):
    url = f"{BASE_URL}/auth/register"
    data = {"username": username, "password": password}
    try:
        response = requests.post(url, json=data)
        if response.status_code == 200:
            return True, response.text
        else:
            return False, response.text
    except requests.exceptions.RequestException as e:
        return False, str(e)

def login_user(username, password):
    url = f"{BASE_URL}/trades"
    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            return False
        else:
            return False
    except requests.exceptions.RequestException:
        return False

def add_trade(username, password, trade_data):
    url = f"{BASE_URL}/trades"
    try:
        response = requests.post(url, json=trade_data, auth=(username, password))
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return None, str(e)

def list_trades(username, password):
    url = f"{BASE_URL}/trades"
    try:
        response = requests.get(url, auth=(username, password))
        if response.status_code == 200:
            return True, response.json()
        else:
            return False, response.text
    except requests.exceptions.RequestException as e:
        return False, str(e)

def update_trade(username, password, trade_id, trade_data):
    url = f"{BASE_URL}/trades/{trade_id}"
    try:
        response = requests.put(url, json=trade_data, auth=(username, password))
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return None, str(e)

def delete_trade(username, password, trade_id):
    url = f"{BASE_URL}/trades/{trade_id}"
    try:
        response = requests.delete(url, auth=(username, password))
        return response.status_code, response.text
    except requests.exceptions.RequestException as e:
        return None, str(e)