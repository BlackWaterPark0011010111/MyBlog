
################################################
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Post

# Регистрация моделей
User = get_user_model()
admin.site.register(Post)

if not admin.site.is_registered(User):
    @admin.register(User)
    class User(UserAdmin):
        pass
#### require 
#################################################