from typing import Dict, List, Optional, Any
from app.Connector.Discord import Discord
from app.Connector.Telegram import Telegram
import requests
import os

class Connectors:
    def __init__(self):
        self._active_connectors: Dict[str, Any] = {}

    def add_connector(self, connector_name: str, connector_instance: Any) -> bool:
        if connector_name.lower() not in self._active_connectors:
            self._active_connectors[connector_name.lower()] = connector_instance
            return True
        return False

    def get_connector(self, connector_name: str) -> Optional[Any]:
        return self._active_connectors.get(connector_name.lower())

    async def start_discord(self, token: str) -> bool:
        discord = Discord(token)
        if self.add_connector(token, discord):
            discord.start()
            return True
        return False

    async def start_telegram(self, token: str) -> bool:
        telegram = Telegram(token)
        if self.add_connector(token, telegram):
            telegram.start()
            return True
        return False

    async def start_connector_by_name(self, connector_name: str, token: str) -> bool:
        if connector_name.lower() == "discord":
            return await self.start_discord(token)
        elif connector_name.lower() == "telegram":
            return await self.start_telegram(token)
        return False
    
def ask_connectors():
    url = os.getenv('PEDOCONTROLLER_API_URL')
    payload = {}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"Message successfully sent to the server: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to the server: {e}")