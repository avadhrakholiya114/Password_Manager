from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import RegitrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# password
def index(request):
    return render(request,"home.html")

def register(request):
    if request.method == "POST":
        form = RegitrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully. Please login to your account')
            return redirect('/login')


    else:
        form = RegitrationForm()
    return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == "POST":
        # form=LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        user_object=User.objects.filter(username=username)
        if not user_object.exists():
            messages.warning(request, "Invalid Credntials.")
            return HttpResponseRedirect(request.path_info)
        user_obj1 = authenticate(username=username, password=password)
        if user_obj1:
            login(request,user_obj1)
            return redirect('/')
        messages.warning(request, "Invalid Credntials.")
        return HttpResponseRedirect(request.path_info)

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})