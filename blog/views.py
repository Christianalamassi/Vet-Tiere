from django.shortcuts import render, get_object_or_404,reverse
from .models import UserInfo
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import userform
# Create your views here.

# Homepage
def home(request):
    return render(request, 'blog/index.html')

#about page
def about(request):
    return render(request, 'blog/about.html')

@login_required
def user(request):
    return render(request, 'blog/user.html')

#Users page
@login_required
def appointment(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "blog/message.html")

    else:
        form = userform()
        return render(request, "blog/appointment.html",{'form':form})


@login_required
def delete_booking(request, Info_id):
    """
    view to delete comment
    """
    form = get_object_or_404(form, id=form_id, user=request.user)
    form.delete()

    messages.success(request, 'You have deleted your appointment!')
    return redirect('blog/appointment.html')
   


@login_required
def message(request):
    if request.method == 'POST':
        pet_names = request.POST['pet_name']
        dates = request.POST['date']
        times = request.POST['time']
        return render(request, "blog/message.html",{
            'pet_names' : pet_names,
            'dates' : dates,
            'times' : times,})
    else:
        return render(request, "blog/user.html")
