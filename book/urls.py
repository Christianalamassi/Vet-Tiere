from django.urls import path
from book import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [ 
    path ('',TemplateView.as_view(template_name='book/index.html'),name='homepage'),
    path('about',views.about, name='about'),
    path('appointment',views.appointment, name='appointment'),
]