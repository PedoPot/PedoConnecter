from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from app.Connector.AbstractConnector import AbstractConnector
import asyncio

class Telegram(AbstractConnector):
    
    def __init__(self, token: str):
        super().__init__()
        self.token = token
        print(f"[DEBUG] Initializing Telegram bot with token: {token}")
        self.application = Application.builder().token(token).build()

    def start(self):
        async def run():
            message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message)
            self.application.add_handler(message_handler)

            await self.application.initialize()
            await self.application.start()
            await self.application.updater.start_polling()

        try:
            loop = asyncio.get_running_loop()
            loop.create_task(run())
        except RuntimeError:
            asyncio.run(run())

    async def handle_message(self, update: Update, context):
        message_content = update.message.text
        chat_id = update.message.chat_id
        message_date = update.message.date.isoformat()
        self.send_message_to_pedo_controller("telegram", chat_id, message_content, message_date)

    async def send_direct_message(self, user_id: int, message: str):
        await self.application.bot.send_message(chat_id=user_id, text=message)