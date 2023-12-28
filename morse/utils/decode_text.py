from typing import Any
from ..models import MorseAudioPath

class TextDecoder():

    def start_lists_coders(self, value_text):
        try:
            self.value_text_code = str(value_text).strip().replace(' ', '').upper()

            list_text = self.translate_text_to_code()
            list_sounds = self.translate_text_to_audio()
            
            return {'list_text': list_text, 'list_files': list_sounds}

        except Exception as e:
            return {'error': str(e), 'status': 500}



    def translate_text_to_code(self):
        try:
            value_text = self.value_text_code
            return [self.get_query_text_code(char) or '#' for char in value_text]

        except Exception as e:
            return {'error': str(e), 'status': 500}


    def translate_text_to_audio(self):
        try:
            value_text = self.value_text_code
            return [self.get_query_audio_path(char) or self.query_default_in_db()['audio_path'] for char in value_text]

        except Exception as e:
            return {'error': str(e), 'status': 500}


    def get_query_text_code(self, char):
        query = MorseAudioPath.objects.filter(name=char).first()
        return query.text_code if query else None

    def get_query_audio_path(self, char):
        query = MorseAudioPath.objects.filter(name=char).first()
        return query.audio_path.url if query else None

    def query_default_in_db(self):
        try:
            query = MorseAudioPath.objects.filter(name='DEFAULT').first()
            return {'name_text': query.name, 'translated_code': query.text_code, 'audio_path': query.audio_path.url} if query else {}

        except Exception as e:
            return {'error': str(e), 'status': 501}
