# urls.py

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import login_view, error_view

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", login_view, name="login_page"),
    path("welcome/", views.welcome, name="welcome"),
    path("select_role/", views.RoleSelectionView.as_view(), name="select_role"),
    path("error/", error_view, name="error_page"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
