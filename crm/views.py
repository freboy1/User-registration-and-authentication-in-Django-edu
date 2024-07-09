from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def homepage(request):
    return render(request, 'crm/index.html')




def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            
            return redirect('my-login')

    context = {'registerform': form}

    return render(request, 'crm/register.html', context)




def my_login(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
    context = {'loginform': form}
    return render(request, 'crm/my-login.html', context)


def user_logout(request):
    logout(request)
    return redirect('')


def dashboard(request):

    return render(request, 'crm/dashboard.html')