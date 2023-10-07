from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegitrationForm
from django.contrib import messages

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

    else:
        form = RegitrationForm()
    return render(request, 'signup.html', {'form': form})
