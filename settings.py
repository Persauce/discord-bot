import os

from dotenv import load_dotenv

load_dotenv()
DISC_CODE = os.getenv("DISCORD_API_TOKEN")
