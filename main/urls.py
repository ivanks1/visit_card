from django.contrib import admin 
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls), # админка
    path('', views.home, name='home'), # начальная страница
    
    path('ru/', views.home_ru, name='home_ru'), 
    path('en/', views.home_en, name='home_en'), # разные языковые версии сайта
    path('kz/', views.home_kz, name='home_kz'),

    path('<str:unknown>/', views.page_not_found, name='page_not_found'), # ошибка 404, обязательно в самый конец!
]
