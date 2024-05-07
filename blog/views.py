from django.shortcuts import render
from .models import patient

# Create your views here.

def home(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def sign(request):
     
    return render(request, "blog/signin.html")

def booking(request):
    if request.method == 'POST':
        day = request.POST['']
        time = request.POST['']
        message = request.POST['']

    return render(request, "blog/book.html")