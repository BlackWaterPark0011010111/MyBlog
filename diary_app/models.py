from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 




class Entry(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='entry_img/', null=True, blank=True)
    people_links = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        title_preview = self.title[:20] + '...' if len(self.title) > 20 else self.title
        text_preview = self.text[:20] + '...' if len(self.text) > 20 else self.text
        author_username = self.author.username if self.author else "No author"
        published_date = self.published_date.strftime('%Y-%m-%d %H:%M:%S') if self.published_date else "No published date"
        image_url = self.image.url if self.image else "No image"
        people_links = self.people_links if self.people_links else "No links"

        return (
            f'Title: {title_preview} | '
            f'Text: {text_preview} | '
            f'Created Date: {self.created_date.strftime("%Y-%m-%d %H:%M:%S")} | '
            f'Published Date: {published_date} | '
            f'Author: {author_username} | '
            f'Image URL: {image_url} | '
            f'People Links: {people_links}'
        )
    #def __str__(self):
    #    people_links = self.people_links if self.people_links else "No links"
    #    image_url = self.image.url if self.image else "No image"
    #    author_username = self.author.username if self.author else "No author"
    #    published_date = self.published_date if self.published_date else "No published date"
    #    
    #    return (
    #        f'People Links: {people_links} | '
    #        f'Image URL: {image_url} | '
    #        f'Author: {author_username} | '
    #        f'Published Date: {published_date} | '
    #        f'Created Date: {self.created_date} | '
    #        f'Text: {self.text} | '
    #        f'Title: {self.title}'
    #    )
    #def __str__(self):
    #    # Ограничиваем длину текста и заголовка до 20 символов для краткости
    #    text_preview = self.text[:20] + '...' if len(self.text) > 20 else self.text
    #    title_preview = self.title[:20] + '...' if len(self.title) > 20 else self.title
    #    
    #    return (f'{self.people_links or "No links"} | '
    #            f'{self.image.url if self.image else "No image"} | '
    #            f'{self.author.username if self.author else "No author"} | '
    #            f'{self.published_date or "No published date"} | '
    #            f'{self.created_date} | '
    #            f'{text_preview} | '
    #            f'{title_preview}')

    class Meta:
        ordering = ['-created_date']  
#class Entry(models.Model):
#    title = models.CharField(max_length=200)
#    content = models.TextField()
#    date_created = models.DateTimeField(auto_now_add=True)
#    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    #Связь с пользователем
    

        

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