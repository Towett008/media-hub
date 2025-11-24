from django.shortcuts import render,redirect
from django.contrib.auth import login, logout, authenticate # Django inbuilt operations that return true or false
from django.contrib.auth.decorators import login_required # returns true or false -> gives permissions to usage of view actions based off user activities
# decorators : functions return othetr functions
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm,UserLoginForm,UserProfileForm

# Create your views here.
def register_views(request):
    #validate if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('media_assets:dashboard')
    if request.method == 'POST':
         # User wantd to register
         form = UserRegistrationForm(request.POST)
         # if user has filled in al required inputs
         if form.is_valid():
             user = form.save() ## submits our user to our db
             login(request,user) ## calls the login action
             messages.success(request,f'Welcome {user.username}! Your account has been successfully created')
             return redirect('media_assets:dashboard')
    else:
        form = UserRegistrationForm() # default http method here is GET
        return render(request, 'accounts/register.html', {'form'} , form)
    

 #log_in view   
def login_views(request):
    #validate if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('media_assets:dashboard')
    if request.method == 'POST':
         # User wantd to register
         form = UserLoginForm(request.POST)
         # if user has filled in al required inputs
         if form.is_valid():
           #pick up entries or username and password
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           # djangomethod authenticate and login my user
           user = authenticate(username, password) # queries db looiking for the user with mentioned credentials
           if user is not None:
               login(request,user)
               messages.success(request,f'Welcome back {username}')
               return redirect('media_assets:dashboard')
          


    else:
        form = UserLoginForm() # default http method here is GET
        return render(request, 'accounts/login.html', {'form'} , form)




        
         

