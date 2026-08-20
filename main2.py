import urllib.request
import urllib.parse
import json
import time

API_TOKEN = '8810291695:AAGwqGrbrvblWxpbmSwN-EO__BcSFLlwQ_w'
BASE_URL = f'https://api.telegram.org/bot{API_TOKEN}'

def get_updates(offset=None):
    url = f'{BASE_URL}/getUpdates?timeout=30'
    if offset:
        url += f'&offset={offset}'
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode('utf-8'))
        return data.get('result', [])
    except Exception:
        return []

def send_message(chat_id, text):
    url = f'{BASE_URL}/sendMessage'
    data = urllib.parse.urlencode({'chat_id': chat_id, 'text': text}).encode('utf-8')
    try:
        req = urllib.request.Request(url, data=data)
        urllib.request.urlopen(req)
    except Exception:
        pass

offset = None
while True:
    updates = get_updates(offset)
    for update in updates:
        offset = update['update_id'] + 1
        if 'message' in update:
            chat_id = update['message']['chat']['id']
            text = update['message'].get('text', '')
            if text == '/start':
                send_message(chat_id, "أهلاً بك في المنقذ العربي2. أرسل (نزيف، اختناق، حروق) للإسعافات.")
            elif 'نزيف' in text:
                send_message(chat_id, "🚨 للنزيف: اضغط بقوة بقطعة قماش نظيفة وارفع الطرف المصاب.")
            elif 'اختناق' in text:
                send_message(chat_id, "🫁 للاختناق: قف خلف المصاب واضغط بقوة أسفل القفص الصدري.")
            elif 'حروق' in text:
                send_message(chat_id, "🔥 للحروق: اغسل بماء فاتر 15 دقيقة ولا تضع ثلجاً أو زيوت.")
    time.sleep(1)
