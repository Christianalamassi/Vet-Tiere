from django.shortcuts import render
from .models import user_info
from django.http import HttpResponse
# Create your views here.

# Homepage
def home(request):
    return render(request, 'blog/index.html')

#about page
def about(request):
    return render(request, 'blog/about.html')

#sign in page
def sign(request):
    #if request.method == GET:
        return render(request, "blog/signin.html")

# log-in page
def login(request):
    if request.method == 'POST':
        fnames = request.POST['fname']
        passwords= request.POST['password']
        return render(request, "blog/login.html")
    else:
        request.HttpResponse("your inter is incorrect! try agian.")

#Users page
def user(request):
    if request.method == 'POST':
        fnames = request.POST['fname']
        dates = request.POST['date']
        times = request.POST['time']

        return render(request, "blog/user.html", {'dates' : dates})
    else :
        request.HttpResponse("your inter is incorrect! try agian.")
        

def appointment(request):
    return render(request, 'blog/appointment.html')