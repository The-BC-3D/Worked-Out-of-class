import requests

server = "http://127.0.0.1:5000"


def register(username, password):
    response = requests.post(
        f"{server}/register",
        json={
            "username": username,
            "password": password
        }
    )

    print(response.json())


def login(username, password):
    response = requests.post(
        f"{server}/login",
        json={
            "username": username,
            "password": password
        }
    )

    print(response.json())


register("Bryce", "TestPassword123")

login("Bryce", "TestPassword123")