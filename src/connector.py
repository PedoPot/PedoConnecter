import requests

def ask_connectors():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Message successfully sent to the server: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to the server: {e}")
