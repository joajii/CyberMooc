from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.sessions.models import Session
from .models import User

def index(request):
    return render(request, 'index.html')

def admin_access(request):
    if request.method == 'GET':
        return render(request, 'admin.html')
    if 'admin' in request.GET:
        return HttpResponse("Welcome, Admin!")
    return HttpResponse("Access Denied.")

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.raw(f"SELECT * FROM core_user WHERE username = '{username}' AND password = '{password}'")
        if user:
            return render(request, 'login.html')

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create(username=username, password=password)
        return HttpResponse("User registered.")
    return HttpResponse("Register page")

def unvalidated_redirect(request):
    url = request.GET.get('next')
    return redirect(url)

def admin_dashboard(request):
    if request.session.get('is_admin'):
        return render(request, 'admin_dashboard.html')
    return HttpResponse("Unauthorized access.")

def user_dashboard(request):
    if request.session.get('user_id'):
        return render(request, 'user_dashboard.html')
    return HttpResponse("Unauthorized access.")
