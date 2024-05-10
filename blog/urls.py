from django.urls import path
from blog import views

urlpatterns = [ 
    path('',views.home, name='homepage'),
    path('singup',views.singup, name='singup'),
    path('message',views.message, name='message'),
    path('login',views.login, name='login'),
    path('about',views.about, name='about'),
    path('userpage',views.user, name='user'),
    path('appointment',views.appointment, name='appointment'),
   ]