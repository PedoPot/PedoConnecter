import requests
import abc
import datetime

class Connector:
    def __init__(self):
        pass

    def send_message_to_pedo_controller(self, connector_name: str, user_id: str, message_content: str, message_date: str):
        url = "https://webhook.site/14762a4c-aca9-4677-b3f9-43ebe9daae5c" #TODO: modify the URL 
        payload = {
            "connector_name": connector_name,
            "user_id": user_id,
            "message_content": message_content,
            "message_date": message_date
        }
        headers = {
            "Content-Type": "application/json"
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            print(f"Message successfully sent to the server: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message to the server: {e}")

    @abc.abstractmethod
    async def send_direct_message(self, user_id: str, message: str):
        pass