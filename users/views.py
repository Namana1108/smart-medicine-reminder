from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Doctor registration view
def doctor_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('add_prescription')
    else:
        form = UserCreationForm()
    return render(request, 'users/doctor_register.html', {'form': form})

# Home view
@login_required
def home(request):
    return render(request, 'users/home.html', {'user': request.user})

