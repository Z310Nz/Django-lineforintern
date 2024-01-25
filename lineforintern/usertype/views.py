from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import json
import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
import base64
from django.contrib import messages
from django.contrib.auth import get_user_model
from .forms import StudentLoginForm, CompanyLoginForm, ProfessorLoginForm
from .models import Student, Company, Professor

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


#======================================Line======================================
def line_login(request):
    # Redirect users to Line login page
    redirect_uri = request.build_absolute_uri(reverse('line_callback'))
    line_login_url = f"https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id={settings.LINE_LOGIN_CHANNEL_ID}&redirect_uri={redirect_uri}&state=state&scope=openid%20profile"
    return redirect(line_login_url)

def line_callback(request):
    # Handle Line login callback
    code = request.GET.get('code')
    if code:
        access_token_url = "https://api.line.me/oauth2/v2.1/token"
        redirect_uri = request.build_absolute_uri(reverse('line_callback'))
        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'client_id': settings.LINE_LOGIN_CHANNEL_ID,
            'client_secret': settings.LINE_LOGIN_CHANNEL_SECRET,
            'redirect_uri': redirect_uri,
        }
        response = requests.post(access_token_url, data=data)
        response_data = response.json()

        # Extract user information
        id_token = response_data.get('id_token')
        user_info = parse_id_token(id_token)

        # Handle user information as needed
        # ...

        return HttpResponse("Line login successful!")

    return HttpResponse("Line login failed.")

def parse_id_token(id_token):
    # Decode and parse Line ID token
    parts = id_token.split('.')
    if len(parts) != 3:
        raise ValueError("Invalid ID token format")

    payload = json.loads(base64.b64decode(parts[1] + '=' * (4 - len(parts[1]) % 4)).decode('utf-8'))
    return payload

#======================================Student======================================
def student_register(request):
    return render(request, 'student/register.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user and user.is_student:
            login(request, user)
            return redirect('student_profile')
        else:
            messages.error(request, 'Invalid login credentials for a student.')
    
    return render(request, 'student/login.html')

def student_profile(request):
    return render(request, 'student/profile.html')

def student_edit_profile(request):
    return render(request, 'student/edit_profile.html')

@require_http_methods(['GET'])
def student_logout(request):
    logout(request)
    return redirect('student_login')

#======================================Company======================================
def company_register(request):
    return render(request, 'company/register.html')

def company_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user and user.is_company:
            login(request, user)
            return redirect('company_profile')
        else:
            messages.error(request, 'Invalid login credentials for a company.')

    return render(request, 'company/login.html')

def company_profile(request):
    return render(request, 'company/profile.html')

def company_edit_profile(request):
    return render(request, 'company/edit_profile.html')

def add_position(request):
    # Add position logic
    return render(request, 'company/add_position.html')

@require_http_methods(['GET'])
def company_logout(request):
    logout(request)
    return redirect('company_login')

#======================================Professor======================================

def professor_dashboard(request):
    # Professor dashboard logic
    return render(request, 'professor/dashboard.html', {})