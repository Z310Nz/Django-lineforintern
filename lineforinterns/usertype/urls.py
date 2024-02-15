# urls.py

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import login_view, error_view, logout_view

urlpatterns = [
    path("", views.home_view, name="home"),
    path("homepage/", views.home_view, name="homepage"),
    path("login/", login_view, name="login_page"),
    path("welcome/<str:username>/", views.welcome, name="welcome"),
    path("error/", error_view, name="error_page"),
    path("profile/<str:role>/<str:username>/", views.profile, name="profile"),
    path("addinfo/<str:role>/<str:username>/", views.addinfo, name="addinfo"),
    # path("editinfo/<str:role>/<str:username>/", views.editinfo, name="editinfo"),
    # path("deleteinfo/<str:role>/<str:username>/", views.deleteinfo, name="deleteinfo"),
    # path("search/", views.search, name="search"),
    # path("searchresult/", views.searchresult, name="searchresult"),
    # path("searchresult/<str:role>/<str:username>/", views.searchresult, name="searchresult"),
    # # path("companyinfo/",include("company.urls")),
    path("addjob/<str:role>/<str:username>/", views.postjob, name="postjob"),
    path("logout/", logout_view, name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
