from django.shortcuts import render, reverse
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie!"}
    return render(request, 'rango/index.html', context=context_dict)
    # return HttpResponse("Rango says hey there partner!<br> <a href='" + reverse('about') + "'>About</a>")


def about(request):
    context_dict = {
        'user_name': "Matt Perrott"
    }
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says this is the about page.<br> <a href='" + reverse('index') + "''>Home</a>")