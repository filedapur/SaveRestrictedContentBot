#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 24563466
API_HASH = "98d3237f74bbda10836ea70d51b8e099"
BOT_TOKEN = "5574629642:AAGZCxVZg4MMkF3x-PLeqEWi4gv9FF9zDHQ"
SESSION = "BAC4TcnqiJI4LO9136Mm9tkzwRpODYtEipu_QGxEP5rXroum1FqWTsDjGeTiTq4vCrIVA2lz6FDmjgzUBrUxexRR6DiwS2eFlpL0A_HFrfFuKa4tjDv4LiAl9O6zmK0J9C7buSjdWpJ_hflYSeu1PquAvRoSNSPBXz1XIW_ZPeveqhuHBBEk2kbj0kgnIWNs73ArP2Y9zM4NtpvsK4ckxJd9PMKnLum1IO0mQYIG7dNlo48acSV99gs1GNFB2BAJ1x2O84ql4jJnfNSoe9KCCwmxi5EBzWR-wE7N_LBGBXKGpcaV31FS0eOBc0BerLggpYsDFfiYavaHCXcTCG4IA-MHAAAAAV069TYA"
FORCESUB = "nnnnnejeje"
AUTH = 5859112246

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
