import requests
import time

from os import getenv
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
BOT_TOKEN = getenv('BOT_TOKEN')

API_URL = 'https://api.telegram.org/bot'
offset = -2
counter = 0
cat_response: requests.Response

PHOTO_REPLY_TEXT = "Ого, ты мне прислал Фото!"
STICKER_REPLY_TEXT = "Ого, ты мне прислал Стикер!"


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']

            if result['message'].get('photo'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={PHOTO_REPLY_TEXT}')
            elif result['message'].get('sticker'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={STICKER_REPLY_TEXT}')
            elif result['message'].get('animation'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Ого, ты мне прислал Гифку!')
            elif result['message'].get('document'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Ого, ты мне прислал файл!')
            elif result['message'].get('video'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Ого, ты мне прислал видео!')
            elif result['message'].get('voice'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Ого, ты мне прислал войс!')
            elif result['message'].get('location'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Ого, ты мне прислал локацию!')
            elif result['message'].get('poll'):
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text=Ого, ты мне прислал опрос!')

    time.sleep(1)
    counter += 1
