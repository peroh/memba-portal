from django.shortcuts import render, reverse
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm

# TODO Update URLs to use revese() function

def index(request):
    category_list_likes = Category.objects.order_by('-likes')[:5]
    category_list_views = Category.objects.order_by('-views')[:5]
    context_dict = {'boldmessage': "Crunchy, creamy, cookie!",
                    'category_by_likes': category_list_likes,
                    'category_by_views': category_list_views}
    return render(request, reverse() ''rango/index.html', context=context_dict)
    # return HttpResponse("Rango says hey there partner!<br> <a href='" + reverse('about') + "'>About</a>")


def about(request):
    context_dict = {
        'user_name': "Matt Perrott"
    }
    return render(request, 'rango/about.html', context=context_dict)
    # return HttpResponse("Rango says this is the about page.<br> <a href='" + reverse('index') + "''>Home</a>")

def show_category(request, category_name_slug):
    try:
        context_dict = {}
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None

    return render(request, 'rango/category.html', context_dict)

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return show_category(request, category_name_slug)
        else:
            print form.errors

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)



