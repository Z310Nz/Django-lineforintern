from django.shortcuts import render, redirect
from .models import CustomUser, Student, StudentProfile, Company, CompanyProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpStudentForm, SignUpCompanyForm, RoleSelectionForm
from django.views.generic import TemplateView
from student.models import StudentInfo
from student.views import register


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
                    return redirect("student_profile")
                elif user.role == CustomUser.Role.COMPANY:
                    return redirect("company_profile")
            else:
                # If user is not registered, create a new user
                new_user = CustomUser.objects.create_user(username=username, password=password)
                new_user.role = CustomUser.Role.STUDENT  # Set the default role for new users
                new_user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("welcome", username=request.user.username)
    else:
        form = LoginForm()
    return render(request, "usertype/login.html", {"form": form})


def welcome(request, username):
    return render(request, "usertype/welcome.html", {"username": username})


class RoleSelectionView(TemplateView):
    template_name = "usertype/select_role.html"

    def post(self, request, *args, **kwargs):
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data["role"]
            # Redirect to error page if form is not valid
            if role not in [choice[0] for choice in CustomUser.Role.choices]:
                return redirect("error_page")

            # Retrieve username and password from session
            username = request.session.get("username")
            password = request.session.get("password")
            if username and password:
                # Create a new user with the selected role
                user = CustomUser.objects.create_user(
                    username=username, password=password
                )
                user.role = role  # Assign the selected role to the user
                user.save()

                # Redirect based on the selected role
                if role == CustomUser.Role.STUDENT:
                    return redirect("student:student_register")
                elif role == CustomUser.Role.COMPANY:
                    return redirect("company_register")
            else:
                # Redirect to an error page if username or password is missing
                return redirect("error_page")
        return render(request, self.template_name, {"form": form})