from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('contact', views.contact_view,name="contact"),
    path('signup', views.handlesignup,name="signup"),
    path('login', views.handlelogin,name="login"),
    path('search', views.search, name="search"),
    path('logout', views.handlelogout,name="logout")

]
