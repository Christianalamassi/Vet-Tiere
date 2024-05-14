from django.shortcuts import render, get_object_or_404
from .models import userInfo
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# Homepage
def home(request):
    return render(request, 'blog/index.html')

#about page
def about(request):
    return render(request, 'blog/about.html')


#Users page
@login_required
def user(request):
    if request.method == 'POST':
        form = userInfo(request.POST)
        if form.is_valid():
            dates = request.POST['date']
            times = request.POST['time']
            return render(request, "blog/message.html",{
            'dates' : dates,
            'times' : times})
    else:
        return render(request, "blog/user.html",context)

def message(request):
    return render(request, 'blog/message.html')     



