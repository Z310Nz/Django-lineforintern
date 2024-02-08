# urls.py

from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path("", login_view, name="login_page"),
    path("welcome/", views.welcome, name="welcome"),
    path("select_role/", views.RoleSelectionView.as_view(), name="select_role"),
]
