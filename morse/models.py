from django.db import models




class Usuario(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    spassword = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
