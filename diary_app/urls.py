#from django.urls import path
#from . import views
#from .views import PanCreateView, PanUpdateView, PanDeleteView
#app_name = 'diary_app'
#urlpatterns = [
#    path('', views.home, name='home'),
#]

# diary_app/urls.py
# diary_app/urls.py



##################################################
from django.urls import path, include

from diary_app.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_view(), name='register'),
]
##################################################