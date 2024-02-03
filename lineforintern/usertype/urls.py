# usertype/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.line_login, name='line_login'),
]
