"""
URL configuration for Diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from diary_app import views
from diary_app.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Главная страница
    path('home/', home, name='home'),  # Главная страница после входа
    path('logout/', views.logout_view, name='logout'),
    path('diary_app/', include('diary_app.urls')),  # Подключаем URLы из приложения diary_app
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)