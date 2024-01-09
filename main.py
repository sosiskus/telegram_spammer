# Telegram Bomber - DociTeam
# YouTube Video : https://youtu.be/pWHHpnPz0jc

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os
import time
import pause
import datetime

API_ID = int(24027111)
API_HASH = str("87519f03ba35d130599dbf59f9096515")
PHONE = str("+37128894819")

TARGETS = ["https://t.me/SoSiSkuS_14", "https://t.me/phoneRigaa", "https://t.me/latvia10", "https://t.me/latgalite", "https://t.me/vipsaleee", "https://t.me/balticmarket1", "https://t.me/tirdzins", "https://t.me/baraholkalatvija", "https://t.me/BigBazzaar", "https://t.me/gribupardot", "https://t.me/buylatvija"]
PHOTO_LOC = str('photo.jpg')
TEXT = str("""📱Есть iPhone?📱
Мы готовы купить у вас этот телефон!
💲Покупаем модели: XS —> 14 Pro Max!
📵Нас интересуют: Заблокированные, разбитые и с дефектами!
💶Предложим хорошую сумму или предлагайте свою цену!""")

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
        # send message with attachment (Supported MediaTypes: Photo, Video, Gif, Document, Audio, Sticker)
        for TARGET in TARGETS:
            try:
                await client.send_file(TARGET, file=PHOTO_LOC, caption=TEXT)
            except:
                print("error in sending message")
        time_now = datetime.datetime.now()
        pause.until(time_now + datetime.timedelta(hours=5))

with client:
    client.loop.run_until_complete(main())
