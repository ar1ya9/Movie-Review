from django.urls import path
from . import views

app_name='Accounts'

urlpatterns = [
    path('reg/',views.register,name='register'),
    path('log/',views.loginu,name='login'),
    path('logout/',views.logoutu,name='logout'),
]