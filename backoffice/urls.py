from django.contrib import admin
from django.contrib.admin import views
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
