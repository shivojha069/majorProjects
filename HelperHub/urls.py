from django.contrib import admin
from django.urls import include, path

from HelperHub import views


urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login_user,name='login'),
    path('logout', views.logout_user,name='logout'),
    path('get-in-touch', views.getInTouch,name='getInTouch'),
    path('about', views.about,name='about'),
    path('register', views.register,name='register'),
]
