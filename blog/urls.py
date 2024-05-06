from django.urls import path
from blog import views

urlpatterns = [ 
    path('',views.home, name='homepage'),
    path('book/',views.booking, name='book'),
    path('user_page',views.sign, name='singin'),
    path('about',views.about, name='about'),
    path('time',views.timetable, name='time'),
    ]