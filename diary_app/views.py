#from django.shortcuts import render
#from django.http import HttpResponse
#
#
## Create your views here.
#def home(request): 
#   return HttpResponse('hello world')
    #diary_app/views.py

# diary_app/views.py


##################################################
from django.contrib.auth import authenticate, login
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import EntryForm
from diary_app.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_posts.html', {'posts': posts})

@login_required
def home(request):
    return render(request, 'diary_app/home.html')

@login_required
def all_entries(request):
    entries = Entry.objects.filter(author=request.user)
    return render(request, 'diary_app/all_entries.html', {'entries': entries})

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
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
    return render(request, 'diary_app/create_entry.html', {'form': form})