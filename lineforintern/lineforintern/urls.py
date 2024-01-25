"""
URL configuration for lineforintern project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from usertype.views import line_login, line_callback

urlpatterns = [
    path('admin/', admin.site.urls),
    path('line_login/', line_login, name='line_login'),
    path('line_callback/', line_callback, name='line_callback'),
    path('line_login/student/', line_login, {'user_type': 'student'}, name='line_login_student'),
    path('line_login/company/', line_login, {'user_type': 'company'}, name='line_login_company'),
    path('line_login/professor/', line_login, {'user_type': 'professor'}, name='line_login_professor'),
    path('line_callback/<user_type>/', line_callback, name='line_callback'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
