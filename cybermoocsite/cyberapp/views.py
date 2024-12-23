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
    if 'admin' in request.POST:
        if request.session.get('is_admin'):
            return redirect('admin_dashboard')
    return HttpResponse("Access Denied.")

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = list(User.objects.raw(f"SELECT * FROM cyberapp_user WHERE username = '{username}' AND password = '{password}'"))
        if user:
            request.session['user_id'] = user[0].id
            request.session['is_admin'] = user[0].is_admin
            if user[0].is_admin:
                return redirect('admin_dashboard')
            return redirect('user_dashboard')
        return HttpResponse("Invalid credentials.")

def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        is_admin = request.POST.get('is_admin', 'off') == 'on'
        User.objects.create(username=username, password=password, is_admin=is_admin)
        return HttpResponse("User registered.")

def unvalidated_redirect(request):
    url = request.GET.get('next')
    return redirect(url)

def admin_dashboard(request):
    if request.session.get('is_admin'):
        return render(request, 'admin-dashboard.html')
    return HttpResponse("Unauthorized access.")

def user_dashboard(request):
    if request.session.get('user_id'):
        return render(request, 'user-dashboard.html')
    return HttpResponse("Unauthorized access.")
