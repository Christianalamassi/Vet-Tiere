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

#appointment system
@login_required
def appointment(request):
    if request.method == 'POST':
        pet_names = request.POST['pet_name']
        dates = request.POST['date']
        oclocks = request.POST['oclock']
        form = UserForm(request.POST)
        if form.is_valid():
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            return render(request, "book/message.html",{
            'pet_names' : pet_names,
            'dates' : dates,
            'oclocks' : oclocks,})
        else:
            return render(request, 'book/appointment.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'book/appointment.html', {'form': form})

#Edition system
@login_required
def edit_appointment(request, pk):
    user = get_object_or_404(UserInfo, id=pk, user=request.user)
    if request.method == 'POST':
        pet_names = request.POST['pet_name']
        dates = request.POST['date']
        oclocks = request.POST['oclock']
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return render(request, "book/message.html",{
            'pet_names' : pet_names,
            'dates' : dates,
            'oclocks' : oclocks,})

    else:
        form = UserForm(instance=booking)

    return render(
        request, 'edit.html', {'form': form, 'user': user}
    )



#deletion system
@login_required
def delete_booking(request):
    """
    view to delete comment
    """
    form = get_object_or_404(form, id=form_id, user=request.user)
    form.delete()

    messages.success(request, 'You have deleted your appointment!')
    return redirect('book/appointment.html')

