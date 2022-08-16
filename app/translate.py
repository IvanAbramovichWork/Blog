import os
import requests
from app import app
from flask_babel import _


def translate(text, dest_language):
    if 'TRANSLATOR_KEY' not in app.config or not app.config['TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured')
    myobj = {
        'folderId': 'b1g7tc9jifgu0mahojpl',
        'texts': [text],
        'targetLanguageCode': dest_language
    }
    head = {
        'Content-Type': "application/json",
        'Authorization': 'Bearer {}'.format(os.environ.get('TRANSLATOR_KEY'))
    }
    r = requests.post(
        "https://translate.api.cloud.yandex.net/translate/v2/translate",
        headers=head, json=myobj)
    if r.status_code != 200:
        return _('the translation service failed')
    return r.json()['translations'][0]['text']
