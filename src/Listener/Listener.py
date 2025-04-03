from src.Listener.Discord import DiscordListener

def main():
    service = DiscordListener()
    service.run()

if __name__ == "__main__":
    main()