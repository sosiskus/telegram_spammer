# Telegram Bomber - DociTeam
# YouTube Video : https://youtu.be/pWHHpnPz0jc

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os
import time
import pause
import datetime

API_ID = int(19434485)
API_HASH = str("deaf79fb8646f05cae3239d58497a3cf")
PHONE = str("+37126425568")

TARGETS = [ "https://t.me/SoSiSkuS_14",
            "https://t.me/buylatvija",
            "https://t.me/gribupardot",
            "https://t.me/latgalite",
            "https://t.me/balticmarket1",
            "https://t.me/baraholkalatvija",
            "https://t.me/tirdzins",
            "https://t.me/tirgus",
            "https://t.me/vipsaleee",
            "https://t.me/MobileRiga",
            "https://t.me/kopatichvapefleamarket" ]
PHOTO_LOC = str('photo.jpg')
TEXT = str("""КУПИМ ВАШ iPHONE

• Предложим хорошую цену 
• Покупаем от X —> 15 Pro Max! 
• Покупаем: Заблокированные, разбитые и с другими дефектами! 
• Так же можем купить другую техникум Apple. 

📍Рига, Юрмала, Салдус. 

PIRKSIM JŪSU iPHONE!

• PIEDĀVĀSIM LABU CENU
• PIRKSTAM NO X —> 15 Pro Max!
• PIRKSTAM: BLOKĒTI, SAPLĒSTI UN AR CITIEM DEFEKTIEM!
• VAR ARĪ IEGĀDĀTIES CITUS APPLE IERĪCES.

📍Rīga, Jūrmala, Saldus!""")

client = TelegramClient('session',API_ID, API_HASH)
client.start()

async def main():
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        try:
            await client.sign_in(PHONE, input('Enter the code : '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password : '))
    while True:
        # if time is from 22:00 to 8:00, then continue
        if datetime.datetime.now().hour >= 22 or datetime.datetime.now().hour <= 8:
            print("Time is from 22:00 to 8:00, so we are waiting")
            time_now = datetime.datetime.now()
            pause.until(time_now + datetime.timedelta(hours=5))
            continue

        # send message with attachment (Supported MediaTypes: Photo, Video, Gif, Document, Audio, Sticker)
        for TARGET in TARGETS:
            try:
                await client.send_file(TARGET, file=PHOTO_LOC, caption=TEXT)
                print("Message sent to ", TARGET)
            except:
                print("error in sending message")
        time_now = datetime.datetime.now()
        pause.until(time_now + datetime.timedelta(hours=5))

with client:
    client.loop.run_until_complete(main())
