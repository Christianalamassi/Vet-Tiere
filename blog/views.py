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


#Users page
def user(request):
    userInfos = userInfo.objects.all()
    context = {
        'userInfos':userInfos
    }
    models = userInfo
    if request.method == 'POST':
        dates = request.POST['date']
        times = request.POST['time']
        return render(request, "blog/message.html",{
            'dates' : dates,
            'times' : times})
    else:
        return render(request, "blog/user.html",context)

def message(request):
    return render(request, 'blog/message.html')     



