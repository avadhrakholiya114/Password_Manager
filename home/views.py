from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import RegitrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .utils import encrypt, decrypt
from .models import user_passsword


# from django.contrib.auth.decorators import login_required


# password
def index(request):
    return render(request, "home.html")


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
        user_object = User.objects.filter(username=username)
        if not user_object.exists():
            messages.warning(request, "Invalid Credntials.")
            return HttpResponseRedirect(request.path_info)
        user_obj1 = authenticate(username=username, password=password)
        if user_obj1:
            login(request, user_obj1)
            return redirect('/')
        messages.warning(request, "Invalid Credntials.")
        return HttpResponseRedirect(request.path_info)

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('/')


def add_password(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = encrypt(request.POST['password'])
        application_type = request.POST['application_type']
        if application_type == "Website":
            website_name = request.POST['website_name']
            website_url = request.POST['website_url']
            user_passsword.objects.create(user=request.user, username_or_email=username, password=password,
                                          app_type=application_type, website_name=website_name, website_url=website_url)
            messages.success(request, 'New password added...!')
        elif application_type == "Desktop Application":
            application_name = request.POST['app_name']
            user_passsword.objects.create(user=request.user, username_or_email=username, password=password,
                                          app_type=application_type, application_name=application_name)
            messages.success(request, 'New password added...!')

        elif application_type == "Game":
            game_name = request.POST['game_name']
            user_passsword.objects.create(user=request.user, username_or_email=username,
                                          password=password, app_type=application_type, game_name=game_name)
            messages.success(request, 'New password added...!')
        elif application_type == "Other":
            other = request.POST['other']
            user_passsword.objects.create(user=request.user, username_or_email=username,
                                          password=password, app_type=application_type, other_name=other)
            messages.success(request, 'New password added...!')
        return redirect('/manage_password')

    return render(request, 'add_pass.html')


def manage(request):
    password_list = user_passsword.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'manage.html', {'password_list': password_list})
