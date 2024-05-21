from django.shortcuts import render, get_object_or_404,reverse, redirect
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

#user page
@login_required
def user(request):
    return render(request, 'book/user.html')

#appointment system
@login_required
def appointment(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID")
            user_info = form.save(commit=False)
            user_info.user = request.user
            user_info.save()
            print("FORM IS SAVED")
            return redirect('message')
        else:
            print("FORM ERRORS: ", form.errors)
            return render(request, 'book/appointment.html', {'form': form})
    else:
        print("GET METHOD")
        form = UserForm()
        return render(request, 'book/appointment.html', {'form': form})


#deletion system
@login_required
def delete_booking(request, Info_id):
    """
    view to delete comment
    """
    form = get_object_or_404(form, id=form_id, user=request.user)
    form.delete()

    messages.success(request, 'You have deleted your appointment!')
    return redirect('book/appointment.html')


#message page that the user receives after submitting an appointment
@login_required
def message(request):
    if request.method =="POST":
        pet_names = request.POST['pet_name']
        dates = request.POST['date']
        oclocks = request.POST['oclock']
    return render(request, "book/message.html")#,{
        #'pet_names' : pet_names,
        #'dates' : dates,
        #'oclocks' : oclocks,})

