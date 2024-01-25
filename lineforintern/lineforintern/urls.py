# lineinternship/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usertype.urls')),
    # Add other URL patterns as needed
]
# lineinternship/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usertype.urls')),
    # Add other URL patterns as needed
]