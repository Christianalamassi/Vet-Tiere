from django.shortcuts import render, redirect, get_object_or_404
from .models import userInfo
from django.views import generic
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

# Homepage
def home(request):
    return render(request, 'blog/index.html')

#about page
def about(request):
    return render(request, 'blog/about.html')


@login_required
def booking_page(request):
    return redirect('user')

#Users page
@login_required
def user(request):
    userInfos = userInfo.objects.all()
    context = {
        'userInfos':userInfos
    }
    models = userInfo
    if request.method == 'POST':
        pet_names = request.POST['pet_name']
        dates = request.POST['date']
        times = request.POST['time']
        #texts = request.POST['text']
        messages.success(request, 'Reservation booked successfully!')
        return render(request, "blog/message.html",{
            'pet_names' : pet_names,
            'dates' : dates,
            'times' : times,})
            #'texts' : texts})
    else:
        return render(request, "blog/user.html",context)

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(userInfo, id=booking_id, user=request.user)
    booking.delete()
   



