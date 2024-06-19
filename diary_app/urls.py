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
from django import views
from django.urls import path, include
from . import views
from diary_app.views import Register, create_entry

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('all_entries/', views.all_entries, name='all_entries'),
    path('create_entry/', views.create_entry, name='create_entry'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
  
    path('entries/new/', create_entry, name='create_entry'),
]
##################################################