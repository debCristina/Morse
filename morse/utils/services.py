
from ..models import AudioCode
import base64
import secrets
import os
from django.conf import settings  

def generate_password(length=32):
    random_bytes = secrets.token_bytes(length)
    base64_encoded = base64.b64encode(random_bytes).decode('utf-8')

    password = ''.join(char for char in base64_encoded if char.isalnum())

    return password[:length]


def save_audio_file(path):
    try:
        filename = 'microphone_audio' + generate_password()

        print(filename, 'filename')
        save_audio = AudioCode(name=filename, file=path)
        save_audio.save()

        print(save_audio.file.url, 'filename url')

        return save_audio.file.url
    except:
        return False
