from django.shortcuts import render, get_object_or_404
from .models import userInfo
from django.views import generic
from django.http import HttpResponse
# Create your views here.

# Homepage
def home(request):
    return render(request, 'blog/index.html')

#about page
def about(request):
    return render(request, 'blog/about.html')

#sign in page
def singup(request):
    if request.method == 'POST':
        nams = request.POST['name']
        user_names = request.POST['user_name']
        E_mails = request.POST['E_maill']
        #phones = request.POST['phone']

        return render(request, "blog/message.html", {
            'names' : names,
            'user_names' : user_names,
            'E_mails'  :E_mails,
            #'phones' : phones,
            })
        return render(request, 'blog/message.html')
    else:
        return render(request, 'blog/singup.html')
        
   
#message appears when whaen the user sign up
def message(request):
    return render(request, 'blog/message.html')

# log-in page
def login(request):
    if request.method == 'POST':
        usernames = request.POST['username']
        passwords= request.POST['password']
        return render(request, "blog/login.html")
    else:
        return render(request, "blog/login.html")

#Users page
def user(request):
    models = userInfo
    if request.method == 'POST':
        appointments = request.POST['appointment']
        times = request.POST['times']
        return render(request, "blog/message.html",{
            'appointments' : appointments,
            'times' : times})
    else:
        return render(request, "blog/user.html")
            
def appointment(request):
    return render(request, 'blog/appointment.html')     

