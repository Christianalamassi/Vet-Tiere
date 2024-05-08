from django.urls import path
from blog import views

urlpatterns = [ 
    path('',views.home, name='homepage'),
    path('signin',views.sign, name='singin'),
    path('login',views.login, name='login'),
    path('about',views.about, name='about'),
    path('user-page',views.user, name='user'),
    path('appointment',views.appointment, name='appointment')
   ]