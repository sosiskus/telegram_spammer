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

TARGETS = ["https://t.me/SoSiSkuS_14"]
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
