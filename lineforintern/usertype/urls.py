# usertype/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.line_login, name='line_login'),
    path('select_role', views.SelectRoleView.as_view(), name='select_role'),
]