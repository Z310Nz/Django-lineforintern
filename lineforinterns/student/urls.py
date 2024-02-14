from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path(
        "student/<str:username>/profile/", views.student_profile, name="student_profile"
    )
]
