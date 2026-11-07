from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('ru/', views.home, {'language': 'ru'}, name='home_ru'),
    path('en/', views.home, {'language': 'en'}, name='home_en'),
    path('kz/', views.home, {'language': 'kz'}, name='home_kz'),
    path('<path:unknown>', views.page_not_found, name='page_not_found'),
]
