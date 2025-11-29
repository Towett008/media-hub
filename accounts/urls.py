from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_views,name='register'),
    path('login/', views.login_views, name='login' ),
    path('logout/', views.logout_view,name='logout'),
    path('profile/',views.profile_view,name='profile'),

    #password reset
    path('password-reset/', views.CustomPasswordResetConfirmview.as_view(),name='password_reset'),
    path('Password-reset/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name ='accounts/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',views.CustomPasswordResetConfirmview.as_view(),name='password_reset_confirm' ),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(
        template_name ='accounts/password_reset_complete.html'
        ),name='password_reset_complete')


]
