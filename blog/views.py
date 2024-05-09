from django.shortcuts import render
#from .models import user_info
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
    if request.method == 'POST':
        fnams = request.POST['fname']
        usernames = request.POST['username']
        emails = request.POST['email']
        phones = request.POST['phone']

        return render(request, "blog/message.html", {
            'fnames' : fnames,
            'usernames' : usernames,
            'emails'  :emails,
            'phones' : phones,
            })
    else:
        return render(request, "blog/signin.html")
   
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
        return render(request, "blog/index.html")

#Users page
def user(request):
    dates = request.POST['date']
    times = request.POST['time']
    return render(request, "blog/user.html")
        

def appointment(request):
    return render(request, 'blog/appointment.html')

