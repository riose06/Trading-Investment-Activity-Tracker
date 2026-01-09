from trading_api_client import (
    register_user,
    login_user,
    add_trade,
    list_trades,
    update_trade,
    delete_trade,
)

def prompt_login():
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    return username, password

def main_menu():
    print("\nChoose an action:")
    print("1. Add Trade")
    print("2. List Trades")
    print("3. Update Trade")
    print("4. Delete Trade")
    print("5. Logout")
    choice = input("Enter number: ").strip()
    return choice

def get_trade_data():
    symbol = input("Symbol: ").strip()
    type_ = input("Type (BUY/SELL): ").strip().upper()
    quantity = int(input("Quantity: "))
    price = float(input("Price: "))
    notes = input("Notes: ").strip()
    return {"symbol": symbol, "type": type_, "quantity": quantity, "price": price, "notes": notes}

def cli():
    print("Welcome to Trading & Investment Tracker CLI")
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter number: ").strip()

        if choice == "1":
            username, password = prompt_login()
            success, msg = register_user(username, password)
            print(msg)
        elif choice == "2":
            username, password = prompt_login()
            if login_user(username, password):
                print(f"Login successful! Welcome {username}")
                while True:
                    choice = main_menu()
                    if choice == "1":
                        trade_data = get_trade_data()
                        status, msg = add_trade(username, password, trade_data)
                        print(f"{status}: {msg}")
                    elif choice == "2":
                        success, trades = list_trades(username, password)
                        if success:
                            print("Your Trades:")
                            for t in trades:
                                print(t)
                        else:
                            print(trades)
                    elif choice == "3":
                        success, trades = list_trades(username, password)
                        if not success or not trades:
                            print("No trades found.")
                            continue
                        for t in trades:
                            print(t)
                        trade_id = input("Enter Trade ID to update: ").strip()
                        trade_data = get_trade_data()
                        status, msg = update_trade(username, password, trade_id, trade_data)
                        print(f"{status}: {msg}")
                    elif choice == "4":
                        success, trades = list_trades(username, password)
                        if not success or not trades:
                            print("No trades found.")
                            continue
                        for t in trades:
                            print(t)
                        trade_id = input("Enter Trade ID to delete: ").strip()
                        status, msg = delete_trade(username, password, trade_id)
                        print(f"{status}: {msg}")
                    elif choice == "5":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid choice.")
            else:
                print("Login failed. Please register first.")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    cli()