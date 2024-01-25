# usertype/urls.py

from django.urls import path, include
from . import views
from .views import company_register

urlpatterns = [
    path('', views.home, name='home'),
    path('student/', include('usertype.student_urls')),
    path('company/', include('usertype.company_urls')),
    path('professor/', views.professor_dashboard, name='professor_dashboard'),
    path('company/register/', company_register, name='register_company'),
]
