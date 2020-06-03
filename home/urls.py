from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('blogs', views.blogs, name="blogs"),
    path('contact', views.contact, name="contact"),
    path('africa', views.africa, name="africa"),
    path('signup', views.handleSignup, name="handleSignup"),
    path('login', views.handleLogin, name="handleLogin"),
    path('logout', views.handleLogout, name="handleLogout"),
]