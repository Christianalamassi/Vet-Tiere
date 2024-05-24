from django.shortcuts import render, get_object_or_404, reverse, redirect
from .models import UserInfo
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
# Create your views here.

# Homepage
def home(request):
    return render(request, 'book/index.html')

#about page
def about(request):
    return render(request, 'book/about.html')

#message page
#Here where the user can find the ifno of the appoinrtment
def message(request):
    users=UserInfo.objects.all()
    return render(request, 'book/message.html', {'users':users})

#appointment system
@login_required
def appointment(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            return redirect('message')
        else:
            return render(request, 'book/appointment.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'book/appointment.html', {'form': form})


#Edition system
@login_required
def edit_appointment(request, pk):
    user = UserInfo.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('message')
    else:
        form = UserForm(instance=user)

    return render(
        request, 'book/edit.html', {'form': form, 'user': user}
    )


#deletion system
@login_required
def delete_appointment(request,pk):
    """
    view to delete appointment
    """
    user = UserInfo.objects.filter(user=request.user).first()
    user.delete()

    messages.success(request, 'You have deleted your appointment!')
    return HttpResponseRedirect(reverse('homepage'))

#delete_confirmation
@login_required
def delete_message(request):
        return render(request, "book/delete_message.html")