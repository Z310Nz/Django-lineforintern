from django.shortcuts import render, redirect
from .models import CustomUser, Student, StudentProfile, Company, CompanyProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def error_view(request):
    return render(request, "usertype/error.html")


def student_profile(request, student_id):
    student = Student.objects.get(student_id=student_id)
    return render(request, "student_profile.html", {"student": student})


def company_profile(request, company_name_eng):
    company = Company.objects.get(company_name_eng=company_name_eng)
    return render(request, "company_profile.html", {"company": company})


def home_view(request):
    return render(request, "usertype/home.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == CustomUser.Role.STUDENT:
                    return redirect("student_profile", username=username)
                elif user.role == CustomUser.Role.COMPANY:
                    return redirect("company_profile")
            else:
                new_user = CustomUser.objects.create_user(
                    username=username, password=password
                )
                new_user.role = form.cleaned_data["role"]
                new_user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("welcome", username=username)
    else:
        form = LoginForm()
    return render(request, "usertype/login.html", {"form": form})


def welcome(request, username):
    user = request.user
    role = request.user.role
    return render(
        request,
        "usertype/welcome.html",
        {"username": username, "user": user, "role": role},
    )


def logout_view(request):
    logout(request)
    return redirect("home")
