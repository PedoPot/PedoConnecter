from src.Connector.Discord import Discord
import os
import time

class DiscordListener:
    def __init__(self):
        self.discord = Discord(
            apiKey=os.getenv('X_API_KEY'),
            apiSecret=os.getenv('X_API_SECRET'),
            accessToken=os.getenv('X_ACCESS_TOKEN'),
            accessSecret=os.getenv('X_ACCESS_SECRET')
        )
        self.discord.connect()

    def start_listening(self):
        """Start listening to DMs"""
        print("Starting DM listener service...")
        self.discord.start_dm_streaming()

    def stop_listening(self):
        """Stop listening to DMs"""
        print("Stopping DM listener service...")
        self.discord.stop_streaming()

    def run(self):
        """Main loop for the listener service"""
        try:
            self.start_listening()
            while True:
                time.sleep(1)  # Keep the service running
        except KeyboardInterrupt:
            print("Shutting down DM listener service...")
            self.stop_listening()
        except Exception as e:
            print(f"Error in DM listener service: {e}")
            self.stop_listening() 