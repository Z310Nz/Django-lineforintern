from django.shortcuts import render, redirect
from .models import CustomUser, Student, StudentProfile, Company, CompanyProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpStudentForm, SignUpCompanyForm, RoleSelectionForm
from django.views.generic import TemplateView


def student_profile(request, student_id):
    student = Student.objects.get(student_id=student_id)
    return render(request, "student_profile.html", {"student": student})


def company_profile(request, company_name_eng):
    company = Company.objects.get(company_name_eng=company_name_eng)
    return render(request, "company_profile.html", {"company": company})


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
                return redirect(
                    "welcome"
                )  # Redirect to welcome page if authentication fails
    else:
        form = LoginForm()
    return render(request, "usertype/login.html", {"form": form})


def welcome(request):
    return render(request, "usertype/welcome.html")


class RoleSelectionView(TemplateView):
    template_name = "usertype/select_role.html"

    def post(self, request, *args, **kwargs):
        form = RoleSelectionForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data["role"]
            if role == "student":
                return redirect("student_registration_page")
            elif role == "company":
                return redirect("company_registration_page")
        return render(request, self.template_name, {"form": form})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = RoleSelectionForm()
        return context
