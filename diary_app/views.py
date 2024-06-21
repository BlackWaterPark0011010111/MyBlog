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
from django.shortcuts import render
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

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
    posts = Entry.objects.filter(author=request.user)
    return render(request, 'home.html', {'posts': posts})
#@login_required
#def home(request):
#    posts = Post.objects.all().order_by('-publish')[:5]  # Получить последние 5 записей, отсортированных по дате публикации
#    return render(request, 'home.html', {'posts': posts})

@login_required
def all_entries(request):
    entries = Entry.objects.all()  
    print('..............',entries)

    return render(request, 'diary_app/home.html', {'posts': entries})
    


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

#class Register(View):
#    template_name = 'registration/register.html'
#
#    def get(self, request):
#        context = {
#            'form': UserCreationForm()
#        }
#        return render(request, self.template_name, context)
#
#    def post(self, request):
#        form = UserCreationForm(request.POST)
#
#        if form.is_valid():
#            form.save()
#            username = form.cleaned_data.get('username')
#            password = form.cleaned_data.get('password1')
#            user = authenticate(username=username, password=password)
#            login(request, user)
#            return redirect('home')
#        context = {
#            'form': form
#        }
#        return render(request, self.template_name, context)
##################################################
def logout_view(request):
    logout(request)
    return redirect('home') 
# diary_app/views.py

@login_required
def create_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.save()
            return redirect('home')
    else:
        form = EntryForm()
    return render(request, 'create_entry.html', {'form': form})     # return HttpResponse('<h1>Hello HttpResponse</h1>')  для тестинга 
#if user is not loged  or registered in rederect to the login   page 
#def all_posts(request):
#    posts = Post.objects.all()
#    return render(request, 'home.html', {'posts': posts})
