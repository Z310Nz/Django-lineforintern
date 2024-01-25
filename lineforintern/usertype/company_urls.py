# usertype/company_urls.py

from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('login/', views.company_login, name='company_login'),
    path('register/', views.company_register, name='company_register'),
    path('profile/', views.company_profile, name='company_profile'),
    path('add_position/', views.add_position, name='add_position'),
    # Add other company-related URL patterns
]
