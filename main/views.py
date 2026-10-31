from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    user_lang = request.COOKIES.get('user_language', 'ru')
    if user_lang not in {'ru', 'en', 'kz'}:
        user_lang = 'ru'
    return redirect(f'/{user_lang}/')

def page_not_found(request, unknown):
    return HttpResponse(f'<h1 style="font-family: Arial">Error 404, page not found: <b style="color: red">/{unknown}</b></h1>')


def home_ru(request):
    return render(request, 'home_ru.html')

def home_en(request):
    return render(request, 'home_en.html')

def home_kz(request):
    return render(request, 'home_kz.html')