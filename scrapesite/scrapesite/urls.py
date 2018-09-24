
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("user/", views.user, name='user'),
    path("main/", views.main, name='main'),
]
