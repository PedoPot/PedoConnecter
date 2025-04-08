import requests
import abc

class Connector:
    def __init__(self):
        pass

    def send_message_to_pedo_controller(self, message: str):
        url = "https://webhook.site/14762a4c-aca9-4677-b3f9-43ebe9daae5c" #TODO: modify the URL 
        payload = {"message": message}
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            print(f"Message successfully sent to the server: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message to the server: {e}")

    @abc.abstractmethod
    async def send_direct_message(self, user_id: str, message: str):
        pass