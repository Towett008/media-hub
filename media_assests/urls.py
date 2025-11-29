from django.urls import path
from . import views

app_name = 'media_assests'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
]