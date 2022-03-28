from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render(request, 'home.html', { 'name': 'Hung'})


def contact_view(request):
    return HttpResponse('<h1>Contact</h1>')


def about_view(request):
    return HttpResponse('<h1>About</h1>')