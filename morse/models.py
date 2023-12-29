from django.db import models




class Usuario(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    spassword = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name



class MorseAudioPath(models.Model):
    name = models.CharField(max_length=50)
    subname =  models.CharField(max_length=50)
    text_code = models.CharField(max_length=50)
    audio_path = models.FileField(upload_to='audio_morse_code', null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    

class AudioCode(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='audio_file_user', null=True, blank=True)

    def __str__(self) -> str:
        return self.name