import os
import json
import hashlib

ACCOUNT_DIR = "Accounts"

os.makedirs(ACCOUNT_DIR, exist_ok=True)


def get_file(username):
    return os.path.join(ACCOUNT_DIR, username + ".txt")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def create_account():
    username = input("Choose username: ").strip()
    password = input("Choose password: ")

    if not username or not password:
        print("Username and password cannot be empty.")
        return

    if any(c in username for c in r'\/:*?"<>|'):
        print("Invalid username.")
        return

    path = get_file(username)

    if os.path.exists(path):
        print("Username already exists.")
        return

    account = {
        "username": username,
        "password": hash_password(password)
    }

    with open(path, "w", encoding="utf-8") as file:
        json.dump(account, file, indent=4)

    print("Account created successfully!")


def login():
    username = input("Username: ").strip()
    password = input("Password: ")

    path = get_file(username)

    if not os.path.exists(path):
        print("Account not found.")
        return

    with open(path, "r", encoding="utf-8") as file:
        account = json.load(file)

    if account["password"] == hash_password(password):
        print(f"Welcome, {username}!")
    else:
        print("Incorrect password.")


def main():
    while True:
        print("\n Select an option for USER log in:")
        print("1. Create User")
        print("2. Log In")
        print("3. Exit")

        choice = input("Select: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            login()

        elif choice == "3":
            print("Exiting.")
            break

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()