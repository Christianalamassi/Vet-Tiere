from django.urls import path
from blog import views

urlpatterns = [ 
    path('',views.home, name='homepage'),
    path('message',views.message, name='message'),
    path('about',views.about, name='about'),
    path('userpage',views.user, name='user'),

   ]