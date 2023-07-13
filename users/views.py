from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

@login_required()
def conduct(request):
    return render(request, 'users/conduct.html')

@login_required()
def membership(request):
    return render(request, 'users/membership.html')

@login_required()
def development(request):
    return render(request, 'users/advocacy.html')

@login_required()
def advocacy(request):
    return render(request, 'users/advocacy.html')

@login_required()
def resources(request):
    return render(request, 'users/resources.html')


