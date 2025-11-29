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
        return redirect('media_assests:dashboard')
    if request.method == 'POST':
         # User wantd to register
         form = UserRegistrationForm(request.POST)
         # if user has filled in al required inputs
         if form.is_valid():
             user = form.save() ## submits our user to our db
             login(request,user) ## calls the login action
             messages.success(request,f'Welcome {user.username}! Your account has been successfully created')
             return redirect('media_assests:dashboard')
    else:
        form = UserRegistrationForm() # default http method here is GET
    return render(request, 'accounts/register.html', {'form': form} )
    

 #log_in view   
def login_views(request):
    #validate if the user is already authenticated
    if request.user.is_authenticated:
        return redirect('media_assests:dashboard')
    if request.method == 'POST':
         # User wantd to register
         form = UserLoginForm(request, data = request.POST)
         # if user has filled in al required inputs
         if form.is_valid():
           #pick up entries or username and password
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           # djangomethod authenticate and login my user
           user = authenticate(request, username=username, password=password) # queries db looking for the user with mentioned credentials
           if user is not None:
               login(request,user)
               messages.success(request,f'Welcome back {username}')
               return redirect('media_assests:dashboard')
          


    else:
        form = UserLoginForm(request) # default http method here is GET
    return render(request, 'accounts/login.html', {'form':form})


@login_required
def logout_view(request):
    # use django inbuilt call 
    logout(request)
    messages.info(request, f"You have logged out!!")
    return redirect('accounts:login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f"Profile saved successfully")
            return redirect('accounts:profile')
    else:
        form = UserProfileForm(instance=request.user)
        
    return render(request, 'accounts/profile.html' , {'form' : form})

class CustomPasswordResetView(PasswordResetView):
    # interface change
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    success_url = reverse_lazy('accounts:password_reset_template')

class CustomPasswordResetConfirmview(PasswordResetConfirmView):
    #interface change
    template_name = 'accounts/password_reset_cofirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete') # this will launch when password is update




        
         

