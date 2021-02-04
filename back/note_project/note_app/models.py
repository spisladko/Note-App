from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    """
    Определяет наш пользовательский класс User.
    Требуется имя пользователя и пароль.
    """
    username = models.CharField(db_index=True, max_length=255, unique=True)
    
    def __str__(self):
        return self.username
        
class Note(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    creation_date = models.DateTimeField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
