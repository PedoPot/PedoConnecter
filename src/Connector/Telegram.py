from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from src.Connector.Connector import Connector
import asyncio

class Telegram(Connector):
    
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
        message = update.message.text
        username = update.message.from_user.first_name
        self.send_message_to_pedo_controller(message)
        print(f"[DEBUG] Message from user: {username}, Content: {message}")

 #       response = f"Hello {user_name}, you said: {user_message}"
 #       print("[DEBUG] Relaying the message to the user...")
 #       await self.send_message(update.message.chat_id, response)

    async def send_direct_message(self, user_id: int, message: str):
        await self.application.bot.send_message(chat_id=user_id, text=message)