from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'crm/index.html')

def register(request):

    return render(request, 'crm/register.html')

def my_login(request):

    return render(request, 'crm/my-login.html')

def dashboard(request):

    return render(request, 'crm/dashboard.html')