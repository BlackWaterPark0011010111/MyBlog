from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# diary_app/models.py
#Добавьте дополнительные поля в модель пользователя для более детальной информации.
class User(AbstractUser):
    # Дополнительные поля для пользователя можно добавить здесь
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.username


#Позволяет пользователям классифицировать записи с помощью тегов.
