from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 



class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    #Связь с пользователем
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-date_created']  
        

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    #created_at = models.DateTimeField(auto_now_add=True)  # Дата и время создания записи
    updated_at = models.DateTimeField(auto_now=True)   
    # Дата и время последнего обновления записи

    
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    

#Позволяет пользователям классифицировать записи с помощью тегов.