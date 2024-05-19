from django.urls import path
from blog import views
from django.contrib.auth.decorators import login_required


urlpatterns = [ 
    path('',views.home, name='homepage'),
    path('about',views.about, name='about'),
    path('userpage',views.user, name='user'),
    path('appointment',views.appointment, name='appointment'),
    path('message',views.message, name='message'),
]