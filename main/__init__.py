#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 28849983
API_HASH = "f57ad31a42a8994f5789b2ad162e3cd4"
BOT_TOKEN = "5574629642:AAGZCxVZg4MMkF3x-PLeqEWi4gv9FF9zDHQ"
SESSION = "1AZWarzYBu46OLTzFMoQp-LGWrjh36BD4hVYpQmIkWQIw0osKNA8_o2R-0UpXD6H6NBmApqV0S3mtzIrEDs3Wg5Rezce3d5qJ5RoWzEDIUYGvxHEep5SOL6vu5D0E-QU4czuAHirBFBvWY1alcK4nIkPmXysGtxVVrD8RUklYbRpiBeFv89BGC-pfF9Ek0C2XHffgrMLU9RZ5fS4ZSH0pgHVD5ZjWAz9LIiDYWv1eDId-t3jZl9WueuiiLDfNJ7i5_HgI2dHwyxqRYaAtEp8TbBmiHqDRw0t-oHNAd3LMk3yIQus4UHLtJcLEArVEY_Cm6aoWkAIbMaM0uXal5jD0VJDz31TwInY="
FORCESUB = "nnnnnejeje"
AUTH = 1812404420

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client(
    session_name=SESSION, 
    api_hash=API_HASH, 
    api_id=API_ID)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
