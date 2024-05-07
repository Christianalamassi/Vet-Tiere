from django.shortcuts import render
from .models import Post
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
    #if request == POST:
        return render(request, "blog/login.html")

#Users page
def booking(request):
    if request.method == 'POST':
        day = request.POST['']
        time = request.POST['']
        message = request.POST['']

    return render(request, "blog/user.html")