from django.contrib import admin
from .models import CompanyInfo, Job, CompanyProfile, Company
from .models import StudentInfo, StudentProfile, Student, CustomUser
from .models import StudentManager, CompanyManager, Interview

# Register your models here.
admin.site.register(CompanyInfo)
admin.site.register(Job)
admin.site.register(CompanyProfile)
admin.site.register(Company)
admin.site.register(StudentInfo)
admin.site.register(StudentProfile)
admin.site.register(Student)
admin.site.register(CustomUser)
# admin.site.register(StudentManager)
# admin.site.register(CompanyManager)
admin.site.register(Interview)
