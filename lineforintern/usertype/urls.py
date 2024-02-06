# usertype/urls.py

from django.urls import path
from .views import LineLoginView, SelectRoleView, LineLoginCallbackView

app_name = 'usertype'

urlpatterns = [
    path('', LineLoginView.as_view(), name='line_login'),
    path('select_role/', SelectRoleView, name='select_role'),
    path('callback/', LineLoginCallbackView.as_view(), name='line_login_callback'),
    # path('student/register/', StudentRegisterView.as_view(), name='student_register'),
    # path('company/register/', CompanyRegisterView.as_view(), name='company_register'),
]