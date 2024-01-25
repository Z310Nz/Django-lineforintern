# usertype/student_urls.py

from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('login/', views.student_login, name='student_login'),
    path('register/', views.student_register, name='student_register'),
    path('profile/', views.student_profile, name='student_profile'),
    # Add other student-related URL patterns
]
