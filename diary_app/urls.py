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
from diary_app.views import Register, create_entry,home,password_reset_view
#from django.contrib import admin
from . import views



urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    #path('admin/', admin.site.urls),
    #path('templates/logout/', views.logout_view, name='logout'),
    path('search/', views.search_entries, name='search_entries'),
    path('templates/logout/', views.logout_view, name='logout'),
    path('templates/home/', home, name='home'),
    path('all_entries/', views.all_entries, name='all_entries'),
    path('create_entry/', views.create_entry, name='create_entry'),
    path('templates/register/', Register.as_view(), name='register'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset/', password_reset_view, name='password_reset'),
    path('entries/new/', create_entry, name='create_entry'),
    #path('entry/<int:entry_id>/', views.all_entries, name='entry_detail'),

]
##################################################