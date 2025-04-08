import discord
from discord.ext import commands
from src.Connector.Connector import Connector
import asyncio

class Discord(Connector):
    def __init__(self, token):
        self.token = token
        self.intents = discord.Intents.default()
        self.intents.messages = True
        self.intents.dm_messages = True
        self.intents.guilds = True
        self.intents.message_content = True

        self.bot = commands.Bot(command_prefix="!", intents=self.intents)

        # Events
        self.bot.event(self.on_ready)
        self.bot.event(self.on_message)

        # Commands
        self.bot.command()(self.send_direct_message)
        self.bot.command()(self.send_server_message)

    async def on_ready(self):
        print(f"{self.bot.user} is connnected.")

    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel) and message.author != self.bot.user:
            user_id = str(message.author.id)
            self.send_message_to_pedo_controller("discord", user_id, message.content, message.created_at.isoformat())

    async def send_direct_message(self, user_id: str, message: str):
        try:
            user = await self.bot.fetch_user(int(user_id))
            await user.send(message)
            print(f"Message sent to {user.name} ({user.id})")
        except Exception as e:
            print(f"Failed to send message to user {user_id}: {e}")

    async def send_server_message(self, ctx, channel_id: int, *, contenu):
        channel = self.bot.get_channel(channel_id)
        if channel:
            await channel.send(contenu)
            await ctx.send("Message sent !")
        else:
            await ctx.send("Canal not found.")

    def start(self):
        try:
            loop = asyncio.get_running_loop()
            loop.create_task(self.bot.start(self.token))
        except RuntimeError:
            asyncio.run(self.bot.start(self.token))
