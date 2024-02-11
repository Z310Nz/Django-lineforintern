# urls.py

from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import login_view, error_view


urlpatterns = [
    path("", views.home_view, name="home"),
    path("login/", login_view, name="login_page"),
    path("welcome/<str:username>/", views.welcome, name="welcome"),
    path("select_role/<str:username>/", views.RoleSelectionView.as_view(), name="select_role"),
    path("error/", error_view, name="error_page"),
    path("studentinfo/",include("student.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
