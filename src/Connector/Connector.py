import requests

class Connector:
    
    def __init__(self):
        pass

    def sendMessageToPedoController(self, message: str):
        url = "https://example.com/api/messages" 
        payload = {"message": message}
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            print(f"Message successfully sent to the server: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send message to the server: {e}")
   
    """        
    def receiveMessageFromPedoController(self, message: str):
        print(f"Received message: {message}")
        self.sendMessage(message)
    """