from typing import Dict, List, Optional, Any
from src.Connector.Discord import Discord
from src.Connector.Telegram import Telegram

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

    def get_all_connectors(self) -> Dict[str, Any]:
        return self._active_connectors

    def get_active_connector_names(self) -> List[str]:
        return list(self._active_connectors.keys())

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