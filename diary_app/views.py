#from django.shortcuts import render
#from django.http import HttpResponse
#
#
## Create your views here.
#def home(request): 
#   return HttpResponse('hello world')
    #diary_app/views.py

# diary_app/views.py
"""add name ensteed mysite, logo , user picture,""" 

##################################################
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordResetForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Entry
from .forms import EntryForm
from diary_app.forms import UserCreationForm
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import logging
from .forms import SearchForm
from django.urls import reverse
logger = logging.getLogger(__name__)
from django.db.models import Q

#def entry_detail(request, entry_id):
#    entry = get_object_or_404(Entry, pk=entry_id)
#    return render(request, 'templates/all_entries.html', {'entry': entry})

def search_entries(request):
    query = request.GET.get('query')
    print(".................", query)
    if query:
        results = Entry.objects.filter(Q(title__icontains=query) | Q(text__icontains=query))
    else:
        results = Entry.objects.none()
    return render(request, 'search_results.html', {'results': results})
#def search_entries(request):
#    query = request.GET.get('query')
#    if query:
#        results = Entry.objects.filter(title__icontains=query)  # Пример поиска по заголовку
#    else:
#        results = Entry.objects.none()
#    return render(request, 'search_results.html', {'results': results})

#ef search_entries(request):
#   query = request.GET.get('query')
#   entries = Entry.objects.filter(title__icontains=query) | Entry.objects.filter(content__icontains=query)
#   return render(request, 'search_results.html', {'entries': entries, 'query': query})



def password_reset_view(request):
    logger.debug('Password reset view called')
    
    if request.method == 'POST':
        logger.debug('POST request received')
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save()
            logger.debug('Form is valid')
            return render(request, 'password_reset_done.html')
        else:
            logger.debug('Form is invalid')
    else:
        logger.debug('GET request received')
        form = PasswordResetForm()

    return render(request, 'password_reset.html', {'form': form})



def password_reset_done(request):
    logger.debug('Password reset done view called')
    return render(request, 'password_reset_done.html')  


@login_required
def home(request):
     return render(request, 'home.html')

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')



@login_required
def all_entries(request):
    entries = Entry.objects.all()  
    print('Entries:', entries)

    return render(request, 'all_entries.html', {'entries': entries})

def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('home')
        else:
            print(form.errors)  
            # Вывод ошибок в консоль для отладки
    else:
        form = EntryForm()
    return render(request, 'create_entry.html', {'form': form})

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)



def logout_view(request):
    logout(request)
    return redirect('home') 