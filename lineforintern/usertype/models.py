from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(UserManager):
    def create_user(self, username, email, password=None, user_type=None, **extra_fields):
        extra_fields.setdefault('is_student', user_type == 'student')
        extra_fields.setdefault('is_company', user_type == 'company')
        extra_fields.setdefault('is_professor', user_type == 'professor')
        return super().create_user(username, email, password=password, **extra_fields)


class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('company', 'Company'),
        ('professor', 'Professor'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    objects = CustomUserManager()

# ==================================Start_Student==================================
class LastJob(models.Model):
    position = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=100)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.description} {self.company} {self.start_date} {self.end_date}"
    
class Skills(models.Model):
    Interested_jobs = models.CharField(max_length=100)
    skill_description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.Interested_jobs} at {self.skill_description}"

class Education(models.Model):
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    gpa = models.CharField(max_length=255)
    english_skill = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.degree} at {self.school_name} {self.gpa} {self.english_skill}"
    
class DateIntern(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date} at {self.end_date}"

class Student(User):
    student_id = models.CharField(max_length=10, unique=True)
    profile_image = models.ImageField(_("Profile Image"), upload_to='profile/', null=True, blank=True)
    sfirst_name = models.CharField(max_length=255)
    slast_name = models.CharField(max_length=255)
    nick_name = models.CharField(max_length=255)
    birthdate = models.DateField(max_length=255)
    gender = models.CharField(max_length=255)
    semail = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    line_id = models.CharField(max_length=255)
    website = models.URLField(max_length=255, blank=True)
    cv = models.URLField(max_length=255)
    last_job = models.ForeignKey(LastJob, on_delete=models.SET_NULL, null=True, blank=True)
    skills = models.ForeignKey(Skills, on_delete=models.SET_NULL, null=True, blank=True)
    education = models.ForeignKey(Education, on_delete=models.SET_NULL, null=True, blank=True)
    date_intern = models.ForeignKey(DateIntern, on_delete=models.SET_NULL, null=True, blank=True)
        
    class Meta:
        verbose_name = 'student'
        default_permissions = ()
        permissions = (
            ('view_profile', 'Can view profile'),
        )
# ==================================End_Student==================================



# ==================================Start_Company==================================
class Address(models.Model):
    address = models.CharField(max_length=100)
    sub_district = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    address_label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address} at {self.province} {self.district} {self.sub_district} {self.postal_code} {self.address_label}"

class AddJob(models.Model):
    job_name = models.CharField(max_length=100)
    job_description = models.CharField(max_length=255) # Qualification
    job_type = models.CharField(max_length=255) # Work place
    job_location = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    job_salary = models.CharField(max_length=255) # Company benefits
    job_date = models.CharField(max_length=255) # Working day
    time_in = models.TimeField()
    time_out = models.TimeField()
    job_qualification = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return f"{self.job_name} at {self.job_description} {self.job_type} {self.job_location} {self.job_salary} {self.job_date}"

class Company(User):
    company_name = models.CharField(max_length=50, unique=True)
    profile_image = models.ImageField(_("Profile Image"), upload_to='profile/', null=True, blank=True)
    company_description = models.CharField(max_length=255)
    Foundation_date = models.DateField()
    Company_type = models.CharField(max_length=255)
    number_employee = models.IntegerField()
    website = models.URLField()
    cemail = models.EmailField()
    Address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    add_job = models.ForeignKey(AddJob, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'company'
        default_permissions = ()
        permissions = (
            ('view_profile', 'Can view profile'),
            ('post_job', 'Can post job'),
        )

# ==================================End_Company==================================
        


# ==================================Start_Professor==================================
class Professor(User):
    professor_id = models.CharField(max_length=10, unique=True)
    class Meta:
        verbose_name = 'professor'
        default_permissions = ()
        permissions = (
            ('view_profile', 'Can view profile'),
            ('view_stats', 'Can view statistics'),
        )
# ==================================End_Professor==================================