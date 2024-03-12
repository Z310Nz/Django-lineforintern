# urls.py

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import error_view, logout_view, search

urlpatterns = [
    path("", views.home_view, name="home"),  # Home page
    path("homepage/", views.home_view, name="homepage"),  # Home page
    path("login/", views.realregister, name="login_page"),  # Login page
    path("reallogin/", views.reallogin, name="reallogin"),  # Signup page
    path("welcome/<str:username>/", views.welcome, name="welcome"),  # Welcome page
    path("error/", error_view, name="error_page"),  # Error page
    path("profile/<str:role>/<str:username>/", views.profile, name="profile"),  # Profile page
    path("addinfo/<str:role>/<str:username>/", views.addinfo, name="addinfo"),  # Add info page
    path("editinfo/<str:role>/<str:username>/", views.editinfo, name="editinfo"),  # Edit info page
    path("viewjob/<str:job_id>/", views.viewjob, name="view_job"),  # View job page
    path("apply/<str:job_id>/", views.applyjob, name="apply_job"),  # apply job page
    path("addjob/<str:role>/<str:username>/", views.postjob, name="postjob"),  # Add job page
    path("companyselect/<str:role>/<str:username>/", views.viewselectcompany, name="companyselect"),  # Company select page
    path("position/<str:role>/<str:username>/", views.positionview, name="position"),  # Position page
    path("home/<str:role>/<str:username>/", views.applyview, name="studentview"),  # Show Student who want to work page
    path("logout/", logout_view, name="logout"),  # Logout page
    path("accounts/", include("allauth.urls")),  # Allauth page
    path("delete/<str:job_id>/", views.deletejob, name="deletejob"),  # Delete job page
    path("edit/<str:job_id>/", views.editjob, name="editjob"),  # Edit job page
    path("approved/<str:match_id>/", views.approved, name="approved"),  # Approved page
    path("rejected/<str:match_id>/", views.rejected, name="rejected"),  # Rejected page
    path("interviewed/<str:match_id>/", views.interviewed, name="interviewed"),  # Interviewed page
    path("interview/<str:match_id>/", views.addschedule, name="addschedule"),  # Interview page
    path("showalljob/", views.viewalljob, name="showalljob"),  # Show all job page
    path("job/search/", search, name='job_search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
