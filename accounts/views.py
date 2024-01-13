from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists(): # exists() is a method that let us know if user is exist
                # set your error message here (like - That username is taken)
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    # set your error message here (like - That email is being used)
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register (I don't want it now)
                    #auth.login(request, user)
                    # set your error message here (like - You are now logged in)
                    #return redirect('index')
                    user.save()
                    # set your error message here (like - You are now registered and can log in)
                    return redirect('login')
        else:
            # set your error message here (like - Passwords do not match)
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            # set your success message here (like - You are now logged in)
            return redirect('index')
        else:
            # set your error message here (like - Invalid credentials)
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        # set your success message here (like - You are now logged out)
        return redirect('index')