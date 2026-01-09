import requests
from requests.auth import HTTPBasicAuth

# === CONFIG ===
BASE_URL = "http://localhost:8080"
USERNAME = "yourusername"   # change this to your registered username
PASSWORD = "yourpassword"   # change this to your password
auth = HTTPBasicAuth(USERNAME, PASSWORD)

# === USER FUNCTIONS ===
def register_user(username, password):
    url = f"{BASE_URL}/auth/register"
    data = {"username": username, "password": password}
    response = requests.post(url, json=data)
    print("Register User:", response.json())  # JSON-safe

# === TRADE FUNCTIONS ===
def add_trade(symbol, trade_type, quantity, price, notes=""):
    url = f"{BASE_URL}/trades"
    data = {
        "symbol": symbol,
        "type": trade_type,
        "quantity": quantity,
        "price": price,
        "notes": notes
    }
    response = requests.post(url, json=data, auth=auth)
    print("Add Trade:", response.json())

def list_trades():
    url = f"{BASE_URL}/trades"
    response = requests.get(url, auth=auth)
    print("List Trades:", response.json())

def get_trade(trade_id):
    url = f"{BASE_URL}/trades/{trade_id}"
    response = requests.get(url, auth=auth)
    print(f"Get Trade {trade_id}:", response.json())

def update_trade(trade_id, symbol=None, trade_type=None, quantity=None, price=None, notes=None):
    url = f"{BASE_URL}/trades/{trade_id}"
    data = {}
    if symbol is not None: data["symbol"] = symbol
    if trade_type is not None: data["type"] = trade_type
    if quantity is not None: data["quantity"] = quantity
    if price is not None: data["price"] = price
    if notes is not None: data["notes"] = notes
    response = requests.put(url, json=data, auth=auth)
    print(f"Update Trade {trade_id}:", response.json())

def delete_trade(trade_id):
    url = f"{BASE_URL}/trades/{trade_id}"
    response = requests.delete(url, auth=auth)
    print(f"Delete Trade {trade_id}:", response.json())


# ---- Example usage ----
if __name__ == "__main__":
    # register_user("ethan", "mypassword123")  # only if you want to register again
    add_trade("GOOGL", "BUY", 2, 2800, "Test trade from Python")
    list_trades()
