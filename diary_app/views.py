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

from diary_app.forms import UserCreationForm


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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'diary_app/home.html')

@login_required
def all_entries(request):
    # Логика для получения всех записей пользователя и их отображения
    return render(request, 'diary_app/all_entries.html')

@login_required
def create_entry(request):
    # Логика для создания новой записи
    if request.method == 'POST':
        # Обработка формы создания записи
        pass  # Ваш код обработки формы здесь

    # Если метод GET, просто отображаем форму создания записи
    return render(request, 'diary_app/create_entry.html')
