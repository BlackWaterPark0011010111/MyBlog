from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    return render(request, "Hello,hello")

def main(request):
    file = loader.get_template("diary_entry.html")
    return HttpResponse(file.render())
