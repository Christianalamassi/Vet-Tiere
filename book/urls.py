from django.urls import path
from book import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [ 
    path ('',TemplateView.as_view(template_name='book/index.html'),name='homepage'),
    path('about',views.about, name='about'),
    path('appointment',views.appointment, name='appointment'),
    path('message', views.message, name="message"),
    path('edit_appointment/<int:pk>/',views.edit_appointment, name='edit_appointment'),
    path('delete_appointment/<int:pk>/', views.delete_appointment, name='delete_appointment'),
    path('delete_message', views.delete_message, name='delete_message')
]