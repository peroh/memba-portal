from django.shortcuts import render


def index(request):
    context_dict = {}
    return render(request, 'portal/index.html', context_dict)
