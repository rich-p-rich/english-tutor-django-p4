# log-in functionality
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def custom_sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home/index.html')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')


def custom_register_account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home/index.html')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})
