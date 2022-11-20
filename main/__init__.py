#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = 25117040
API_HASH = "d1cfa64ebbb012620a69b133a2428c25"
BOT_TOKEN = "5766048103:AAGd00y5SRv8z_RfVDWdHHSsMxkzwKs-62o"
SESSION = "AQAhKoXJrBi3S63HT7NzYjyGvR_fk4LBJrPuWMyo_4DiR3pCLosLx5G8Oe135wJBLz7u0iBV45uD4dYGWir7RtnmbaqEBdU278eIglEC8xYAyb8AYKrgvLCmJsoi7HfG8zKew167-1z1dlhMH2OTMH6c5_N4Omngh3LjSjCnf25yrQ7otHRD_Yz9raCYVWx2A_5LjFAqCX1HTrLwrV1YIB7MZS_B2TTqqx88waXx2qo8D7lWp6EbGD_QqFbcT2smQd0E4ynm-9rg4NSD5bv59m2ikuOYTppqbgeEl0c22E7N6bNKd55O-KY0aUP-17HjpaP-J46oVjvoO0E0118N0c3OAAAAAUYLukUA"
FORCESUB = "frcjoin"
AUTH = 5470140997

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
