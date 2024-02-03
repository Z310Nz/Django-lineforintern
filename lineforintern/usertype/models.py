# usertype/models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    line_user_id = models.CharField(max_length=255, unique=True)
    display_name = models.CharField(max_length=255)
    # สามารถเพิ่มฟิลด์อื่น ๆ ตามความต้องการ

    def __str__(self):
        return self.display_name
