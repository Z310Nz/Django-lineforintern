from django.shortcuts import render
from .models import StudentInfo
from django.views.generic import CreateView
from .forms import StudentInfoForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = StudentInfoForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = StudentInfoForm()
    return render(request, 'student/student_register.html.html', {'form': form})

class StudentInfoCreateView(CreateView):
    model = StudentInfo
    form_class = StudentInfoForm
    template_name = 'student/student_register.html'
    success_url = reverse_lazy('login_page')