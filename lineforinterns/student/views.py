from django.shortcuts import render
from .models import StudentInfo
from django.views.generic import CreateView
from .forms import StudentInfoForm, SignUpStudentForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.


def register(request):
    if request.method == "POST":
        form = SignUpStudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect(
                "login"
            )  # Redirect to the login page after successful registration
    else:
        form = StudentInfoForm()
    return render(request, "student/student_register.html", {"form": form})


def student_profile(request, student_id):
    student = StudentInfo.objects.get(student_id=student_id)
    return render(request, "student_profile.html", {"student": student})


def apply_for_work(request):
    pass
