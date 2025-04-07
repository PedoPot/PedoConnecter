from telegram import Update
from telegram.ext import Application, MessageHandler, filters
from src.Connector.Connector import Connector

# This class is a connector for Telegram
class Telegram(Connector):
    
    def __init__(self, token: str):
        super().__init__()
        self.token = token
        print(f"[DEBUG] Initializing Telegram bot with token: {token}")
        self.application = Application.builder().token(token).build()

    # This method adds handlers
    def start(self):
        print("[DEBUG] Starting the bot and adding handlers...")
        message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, self.handleMessage)
        self.application.add_handler(message_handler)
        print("[DEBUG] Message handler added.")
        
        self.application.run_polling()
        print("[DEBUG] Bot is now polling for updates.")

    # handleMessage is called when a message is received
    async def handleMessage(self, update: Update, context):
        print("[DEBUG] Received a message.")
        user_message = update.message.text
        user_name = update.message.from_user.first_name
        print(f"[DEBUG] Message from user: {user_name}, Content: {user_message}")
        response = f"Hello {user_name}, you said: {user_message}"
        #self.sendMessageToPedoController(user_message)
        
        #relay the message to the user
        print("[DEBUG] Relaying the message to the user...")
        await self.sendMessage(update.message.chat_id, response)

    # This method sends a message in the chat
    async def sendMessage(self, chat_id: int, text: str):
        print(f"[DEBUG] Sending message to chat_id {chat_id}: {text}")
        await self.application.bot.send_message(chat_id=chat_id, text=text)

   
bot = Telegram("")
bot.start()