from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_data = ((1, "Student"), (2, "company"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    email = models.EmailField(unique=True)