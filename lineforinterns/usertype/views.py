from django.shortcuts import render, redirect
from .models import (
    CustomUser,
    Student,
    StudentProfile,
    StudentInfo,
    Company,
    CompanyProfile,
    CompanyInfo,
    Job,
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpStudentForm, SignUpCompanyForm, PostJobForm
from django.views.generic import TemplateView
from student.views import register
from django.shortcuts import get_object_or_404


def error_view(request):
    return render(request, "usertype/error.html")


def company_profile(request, company_name_eng):
    company = Company.objects.get(company_name_eng=company_name_eng)
    return render(request, "company_profile.html", {"company": company})


def home_view(request):
    return render(request, "usertype/home.html")


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == CustomUser.Role.STUDENT:
                    return redirect(
                        "profile", username=username, role=user.role
                    )  # แก้ไขที่นี่
                elif user.role == CustomUser.Role.COMPANY:
                    return redirect("profile", username=username, role=user.role)
            else:
                new_user = CustomUser.objects.create_user(
                    username=username, password=password
                )
                new_user.role = form.cleaned_data["role"]
                new_user.save()
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("profile", username=username, role=user.role)  # แก้ไขที่นี่
    else:
        form = LoginForm()
    return render(request, "usertype/login.html", {"form": form})


@login_required
def welcome(request, username):
    user = request.user
    role = request.user.role
    return render(
        request,
        "usertype/welcome.html",
        {"username": username, "user": user, "role": role},
    )


def logout_view(request):
    logout(request)
    return redirect("home")


def profile(request, role, username):
    user = request.user
    student = None
    company = None
    context = {
        "role": role,
        "username": username,
    }

    # หาก user เป็นนักเรียน
    if user.role == CustomUser.Role.STUDENT:
        try:
            student = StudentProfile.objects.get(user__username=username)  # แก้ไขตรงนี้
        except StudentProfile.DoesNotExist:
            pass
    # หาก user เป็นบริษัท
    elif user.role == CustomUser.Role.COMPANY:
        try:
            company = CompanyProfile.objects.get(user__username=username)  # แก้ไขตรงนี้
        except CompanyProfile.DoesNotExist:
            pass

    if request.method == "POST":
        form = SignUpStudentForm(request.POST, initial={"username": user.username})
        if form.is_valid():
            form.save()
            return redirect("welcome", username=user.username)
    else:
        form = SignUpStudentForm(initial={"username": user.username})

    return render(
        request,
        "userweb/profile.html",
        {
            "form": form,
            "student": student,
            "company": company,
            "user": user,
            "context": context,
        },
    )

def addinfo(request, role, username):
    user = request.user
    student = None
    company = None
    context = {
        "role": role,
        "username": username,
    }
    
    if user.role == "STUDENT":
        form = SignUpStudentForm(request.POST or None, request.FILES or None, initial={"username": user.username})
        if request.method == "POST" and form.is_valid():
            profile_image = form.cleaned_data["profile"]
            cv = form.cleaned_data["cv"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            nick_name = form.cleaned_data["nick_name"]
            student_id = form.cleaned_data["student_id"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            gender = form.cleaned_data["gender"]
            birthday = form.cleaned_data["birthday"]
            last_job = form.cleaned_data["last_job"]
            intern_company = form.cleaned_data["intern_company"]
            interest_job = form.cleaned_data["interest_job"]
            skill = form.cleaned_data["skill"]
            eng_skill = form.cleaned_data["eng_skill"]
            university = form.cleaned_data["university"]
            faculty = form.cleaned_data["faculty"]
            major = form.cleaned_data["major"]
            intern_start = form.cleaned_data["intern_start"]
            intern_end = form.cleaned_data["intern_end"]

            profile = StudentInfo.objects.create(
                profile=profile_image,
                cv=cv,
                first_name=first_name,
                last_name=last_name,
                nick_name=nick_name,
                student_id=student_id,
                email=email,
                phone=phone,
                gender=gender,
                birthday=birthday,
                last_job=last_job,
                intern_company=intern_company,
                interest_job=interest_job,
                skill=skill,
                eng_skill=eng_skill,
                university=university,
                faculty=faculty,
                major=major,
                intern_start=intern_start,
                intern_end=intern_end,
            )
            profile.save()

            student = StudentProfile()
            student.user = request.user
            student.studentinfo = profile
            student.save()

            return redirect("profile", username=user.username, role=user.role)

    elif user.role == "COMPANY":
        form = SignUpCompanyForm(request.POST or None, request.FILES or None, initial={"username": user.username})
        if request.method == "POST" and form.is_valid():
            print("1")
            company_logo = form.cleaned_data["logoc"]
            company_eng = form.cleaned_data["company_name_eng"]
            company_thai = form.cleaned_data["company_name_thai"]
            company_info = form.cleaned_data["company_des"]
            foundation = form.cleaned_data["foundation_date"]
            employees = form.cleaned_data["number_of_employees"]
            websitec = form.cleaned_data["website"]
            emailc = form.cleaned_data["email"]
            address = form.cleaned_data["address"]
            sub_dis = form.cleaned_data["sub_district"]
            district = form.cleaned_data["district"]
            country = form.cleaned_data["country"]
            province = form.cleaned_data["province"]
            postal_code = form.cleaned_data["postal_code"]
            line_id = form.cleaned_data["line_id"]
            print("2")
            profilec = CompanyInfo.objects.create(
                logoc=company_logo,
                company_name_eng=company_eng,
                company_name_thai=company_thai,
                company_des=company_info,
                foundation_date=foundation,
                number_of_employees=employees,
                website=websitec,
                email=emailc,
                address=address,
                country=country,
                province=province,
                postal_code=postal_code,
                line_id=line_id,
                sub_sub_district=sub_dis,
                district=district,
            )
            print("3")
            profilec.save()
            company = CompanyProfile()
            company.user = request.user
            company.companyinfo = profilec
            company.save()
            print(profilec)
            return redirect("profile", username=user.username, role=user.role)

    return render(
        request,
        "userweb/addinfo.html",
        {
            "form": form,
            "student": student,
            "company": company,
            "user": user,
            "context": context,
        },
    )

def postjob(request, role, username):
    user = request.user
    student = None
    company = None
    context = {
        "role": role,
        "username": username,
    }
    form = PostJobForm(request.POST or None, request.FILES or None, initial={"username": user.username})
    if request.method == "POST" and form.is_valid():
        job_name = form.cleaned_data["jobname"]
        job_des = form.cleaned_data["jobdes"]
        work_type = form.cleaned_data["worktype"]
        bene_fit = form.cleaned_data["benefit"]
        work_start = form.cleaned_data["workstart"]
        work_end = form.cleaned_data["workend"]
        work_day = form.cleaned_data["workday"]
        require = form.cleaned_data["requirement"]
        qualifi = form.cleaned_data["qualifications"]
        skill = form.cleaned_data["skills"]

        job = Job.objects.create(
            jobname=job_name,
            jobdes=job_des,
            worktype=work_type,
            benefit=bene_fit,
            workstart=work_start,
            workend=work_end,
            workday=work_day,
            requirement=require,
            qualifications=qualifi,
            skills=skill,
        )
        job.save()
        company_profile = get_object_or_404(CompanyProfile, user=user)  # ดึงข้อมูลโปรไฟล์บริษัทของผู้ใช้ที่เข้าสู่ระบบ
        company_info = company_profile.companyinfo  # ดึงข้อมูล CompanyInfo ของบริษัท
        company_info.jobs.add(job)  # เพิ่ม job ใหม่ในบริษัท

        return redirect("profile", username=user.username, role=user.role)
        
    
    return render(
        request,
        "userweb/post_jobs.html",
        {
            "form": form,
            "student": student,
            "company": company,
            "user": user,
            "context": context,
        },
    )
        

    #         student = StudentProfile()
    #         student.user = request.user
    #         student.studentinfo = profile
    #         student.save()

    #         return redirect("profile", username=user.username, role=user.role)
    # return render(
    #     request,
    #     "userweb/addinfo.html",
    #     {
    #         "form": form,
    #         "student": student,
    #         "company": company,
    #         "user": user,
    #         "context": context,
    #     },
    # )