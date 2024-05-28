from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserForm
from .models import UserInfo


# Create your views here.

# Homepage
def home(request):
    """render to hompage"""
    return render(request, 'book/index.html')


# about-us page
def about(request):
    """render to about us page"""
    return render(request, 'book/about.html')


# message page
def message(request):
    """this displays a message to the user includes info of the appointment.
    **Template**
    template:`book/message.html`"""
    form = UserInfo.objects.filter(user=request.user).first
    return render(request, 'book/message.html', {'form': form})


# appointment system
@login_required
def appointment(request):
    """render the panel of the appointment system.
    allows the users to request
    displays an individual instance model:`book.UserInfo`
    **Context**
    ``UserInfo``
    the most recent instence model:`book.UserInfo`
    ``UserForm``
    an instence of form:`book.UserForm`
    **redirect**
    an instence of view :`book.message`
    **Template**
    templat:`book/appointment.html`
    """
    if request.method == 'POST':
        form = UserForm(request.POST, request=request)
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


# Edition system
@login_required
def edit_appointment(request, pk):
    """displays a panel of the appointment system.
    allows the users to update
    **Template**
    template:`book/edit.html`"""
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


# deletion system
@login_required
def delete_appointment(request, pk):

    """displays a panel of the appointment system.
    allows the users to delete
    """

    user = UserInfo.objects.filter(user=request.user).first()
    user.delete()

    messages.success(request, 'You have deleted your appointment!')
    return HttpResponseRedirect(reverse('homepage'))


# delete_confirmation
@login_required
def delete_message(request):
    """this displays a message to the user to confirm the deletion.
    **Template**
    template:`book/delete_message.html`
    """
    return render(request, "book/delete_message.html")
