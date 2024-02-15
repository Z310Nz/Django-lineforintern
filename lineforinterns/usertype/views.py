from django.shortcuts import render, redirect
from .models import (
    CustomUser,
    Student,
    StudentProfile,
    StudentInfo,
    Company,
    CompanyProfile,
    CompanyInfo,
    Job,
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpStudentForm, SignUpCompanyForm
from django.views.generic import TemplateView
from student.views import register


def error_view(request):
    return render(request, "usertype/error.html")


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
                    return redirect(
                        "profile", username=username, role=user.role
                    )  # แก้ไขที่นี่
                elif user.role == CustomUser.Role.COMPANY:
                    return redirect("profile", username=username, role=user.role)
            else:
                new_user = CustomUser.objects.create_user(
                    username=username, password=password
                )
                new_user.role = form.cleaned_data["role"]
                new_user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("profile", username=username, role=user.role)  # แก้ไขที่นี่
    else:
        form = LoginForm()
    return render(request, "usertype/login.html", {"form": form})


@login_required
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


def profile(request, role, username):
    user = request.user
    student = None
    company = None
    context = {
        "role": role,
        "username": username,
    }

    # หาก user เป็นนักเรียน
    if user.role == CustomUser.Role.STUDENT:
        try:
            student = Student.objects.get(username=username)  # แก้ไขตรงนี้
        except Student.DoesNotExist:
            pass
    # หาก user เป็นบริษัท
    elif user.role == CustomUser.Role.COMPANY:
        try:
            company = Company.objects.get(username=username)  # แก้ไขตรงนี้
        except Company.DoesNotExist:
            pass

    if request.method == "POST":
        form = SignUpStudentForm(request.POST, initial={"username": user.username})
        if form.is_valid():
            form.save()
            return redirect("welcome", username=user.username)
    else:
        form = SignUpStudentForm(initial={"username": user.username})

    return render(
        request,
        "userweb/profile.html",
        {
            "form": form,
            "student": student,
            "company": company,
            "user": user,
            "context": context,
        },
    )

def addinfo(request, role, username):
    user = request.user
    student = None
    company = None
    context = {
        "role": role,
        "username": username,
    }
    if request.method == "POST":
        form = SignUpStudentForm(
            request.POST, request.FILES, initial={"username": user.username}
        )
        if form.is_valid():
            profile_image = form.cleaned_data["profile"]
            cv = form.cleaned_data["cv"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            nick_name = form.cleaned_data["nick_name"]
            student_id = form.cleaned_data["student_id"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            gender = form.cleaned_data["gender"]
            birthday = form.cleaned_data["birthday"]
            last_job = form.cleaned_data["last_job"]
            intern_company = form.cleaned_data["intern_company"]
            interest_job = form.cleaned_data["interest_job"]
            skill = form.cleaned_data["skill"]
            eng_skill = form.cleaned_data["eng_skill"]
            university = form.cleaned_data["university"]
            faculty = form.cleaned_data["faculty"]
            major = form.cleaned_data["major"]
            intern_start = form.cleaned_data["internship_start"]
            intern_end = form.cleaned_data["internship_end"]

            # Create and save StudentInfo object
            profile = StudentInfo.objects.create(
                profile=profile_image,
                cv=cv,
                first_name=first_name,
                last_name=last_name,
                nick_name=nick_name,
                student_id=student_id,
                email=email,
                phone=phone,
                gender=gender,
                birthday=birthday,
                last_job=last_job,
                intern_company=intern_company,
                interest_job=interest_job,
                skill=skill,
                eng_skill=eng_skill,
                university=university,
                faculty=faculty,
                major=major,
                intern_start=intern_start,
                intern_end=intern_end,
            )
            profile.save()
            return redirect("profile", username=user.username)
    else:
        form = SignUpCompanyForm(initial={"username": user.username})
        form.is_valid()
        

    return render(
        request,
        "userweb/addinfo.html",
        {
            "form": form,
            "student": student,
            "company": company,
            "user": user,
            "context": context,
        },
    )
