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
    Interview,
    Matching,
)
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import (
    LoginForm,
    SignUpStudentForm,
    SignUpCompanyForm,
    PostJobForm,
    InterviewForm,
    EditStudentForm,
    EditCompanyForm,
    JobSearchForm,
    RealLoginForm,
)
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from itertools import groupby, zip_longest
from django.db.models import Q
from django.contrib import messages


def error_view(request):
    return render(request, "usertype/error.html")


def company_profile(request, company_name_eng):
    company = Company.objects.get(company_name_eng=company_name_eng)
    return render(request, "company_profile.html", {"company": company})


def home_view(request):
    jobs = Job.objects.all()
    return render(request, "usertype/home.html", {"jobs": jobs})


def realregister(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            role = form.cleaned_data["role"]
            
            # Check if the user already exists
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken.')
                return redirect('reallogin')
            
            # Create the new user
            new_user = CustomUser.objects.create_user(username=username, password=password, role=role)
            
            # Authenticate and login the user with the specified backend
            user = authenticate(request, username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            messages.success(request, 'You have successfully registered and logged in! Welcome to InternSE!')
            return redirect("profile", username=username, role=role)
    else:
        form = LoginForm()
    context = {
        'form': form,
        'roles': CustomUser.Role.choices,
    }
    return render(request, "usertype/register.html", context)

def reallogin(request):
    if request.method == "POST":
        form = RealLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == CustomUser.Role.STUDENT:
                    messages.success(request, 'You have successfully logged in! Welcome to InternSE!')
                    return redirect("profile", username=username, role=user.role)
                elif user.role == CustomUser.Role.COMPANY:
                    messages.success(request, 'You have successfully logged in! Welcome to InternSE!')
                    return redirect("profile", username=username, role=user.role)
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = RealLoginForm()
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


@login_required
def logout_view(request):
    logout(request)
    return redirect("home")


@login_required
def profile(request, role, username):
    user = request.user
    student = None
    company = None
    jobs = None

    context = {
        "role": role,
        "username": username,
    }

    if user.role == CustomUser.Role.STUDENT:
        try:
            student = StudentProfile.objects.get(user__username=username)
            # Retrieve all jobs available
            jobs = Job.objects.all()
        except StudentProfile.DoesNotExist:
            pass
    elif user.role == CustomUser.Role.COMPANY:
        try:
            company = CompanyProfile.objects.get(user__username=username)
            # Retrieve jobs related to the company
            jobs = Job.objects.all()
        except CompanyProfile.DoesNotExist:
            pass

    if request.method == "POST":
        form = SignUpStudentForm(request.POST, initial={"username": user.username})
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was successfully updated!')
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
            "jobs": jobs,  # Pass jobs to the template
            "user": user,
            "context": context,
        },
    )


@login_required
def addinfo(request, role, username):
    user = request.user
    student = None
    company = None
    context = {
        "role": role,
        "username": username,
    }

    if user.role == "STUDENT":
        form = SignUpStudentForm(
            request.POST or None,
            request.FILES or None,
            initial={"username": user.username},
        )
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
            skill = form.cleaned_data["skill"]
            eng_skill = form.cleaned_data["eng_skill"]
            university = form.cleaned_data["university"]
            faculty = form.cleaned_data["faculty"]
            major = form.cleaned_data["major"]
            interest_job = form.cleaned_data("interest_job")

            last_job = form.cleaned_data.get("last_job", "N/A")
            intern_company = form.cleaned_data.get("intern_company", "N/A")
            intern_start = form.cleaned_data.get("intern_start", None)
            intern_end = form.cleaned_data.get("intern_end", None)

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
                skill=skill,
                eng_skill=eng_skill,
                university=university,
                faculty=faculty,
                major=major,
                intern_start=intern_start,
                intern_end=intern_end,
                interest_job=interest_job,
            )
            profile.save()

            student = StudentProfile()
            student.user = request.user
            student.studentinfo = profile
            student.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect("profile", username=user.username, role=user.role)

    elif user.role == "COMPANY":
        form = SignUpCompanyForm(
            request.POST or None,
            request.FILES or None,
            initial={"username": user.username},
        )
        if request.method == "POST" and form.is_valid():
            company_logo = form.cleaned_data["profile"]
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
            province = form.cleaned_data["province"]
            postal_code = form.cleaned_data["postal_code"]
            line_id = form.cleaned_data["line_id"]
            phone = form.cleaned_data["phone"]
            profilec = CompanyInfo.objects.create(
                profile=company_logo,
                company_name_eng=company_eng,
                company_name_thai=company_thai,
                company_des=company_info,
                foundation_date=foundation,
                number_of_employees=employees,
                website=websitec,
                email=emailc,
                address=address,
                province=province,
                postal_code=postal_code,
                line_id=line_id,
                sub_district=sub_dis,
                district=district,
                phone=phone,
            )
            profilec.save()
            company = CompanyProfile()
            company.user = request.user
            company.companyinfo = profilec
            company.save()
            messages.success(request, 'Your profile was successfully updated!')
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


@login_required
def editinfo(request, role, username):
    user = request.user
    student = None
    company = None

    context = {
        "role": role,
        "username": username,
    }

    if user.role == CustomUser.Role.STUDENT:
        studentinfo = StudentProfile.objects.get(user=user)
        form = EditStudentForm( request.POST or None, request.FILES or None, instance=studentinfo.studentinfo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect("profile", username=user.username, role=role)
        else:
            messages.error(request, 'Please correct the error below.')

    elif user.role == CustomUser.Role.COMPANY:
        companyinfo = CompanyProfile.objects.get(user=user)
        form = EditCompanyForm(request.POST or None, request.FILES or None, instance=companyinfo.companyinfo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect("profile", username=user.username, role=role)
        else:
            messages.error(request, 'Please correct the error below.')

    return render(
        request,
        "userweb/editinfo.html",
        {
            "form": form,
            "user": user,
            "context": context,
            "student": student,
            "company": company,
        },
    )





@login_required
def postjob(request, role, username):
    user = request.user
    student = None
    company = None
    context = {
        "role": role,
        "username": username,
    }
    form = PostJobForm(
        request.POST or None, request.FILES or None, initial={"username": user.username})
    if request.method == "POST" and form.is_valid():
        job_name = form.cleaned_data["jobname"]
        job_des = form.cleaned_data["jobdes"]
        work_type = form.cleaned_data["worktype"]
        bene_fit = form.cleaned_data["benefit"]
        work_start = form.cleaned_data["workstart"]
        work_end = form.cleaned_data["workend"]
        work_day = form.cleaned_data["workday"]
        require = form.cleaned_data["requirement"]
        skill = form.cleaned_data["skills"]
        com = form.cleaned_data["company"]
        cit = form.cleaned_data["city"]
        cou = form.cleaned_data["country"]

        job = Job.objects.create(
            jobname=job_name,
            jobdes=job_des,
            worktype=work_type,
            benefit=bene_fit,
            workstart=work_start,
            workend=work_end,
            workday=work_day,
            requirement=require,
            skills=skill,
            company=com,
            city=cit,
            country=cou,
        )
        job.save()
        company_profile = get_object_or_404(CompanyProfile, user=user)
        company_info = company_profile
        company_info.job.add(job)
        messages.success(request, 'Your job was successfully posted!')
        return redirect("position", username=user.username, role=user.role)

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


def editjob(request, job_id):
    job = Job.objects.get(id=job_id)
    form = PostJobForm(request.POST or None, request.FILES or None, instance=job)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, 'Your job was successfully updated!')
        return redirect("position", username=request.user.username, role=request.user.role)
    return render(request, "userweb/post_jobs.html", {"form": form, "job": job})

def deletejob (request, job_id):
    job = Job.objects.get(id=job_id)
    job.delete()
    messages.warning(request, 'Your job was deleted!')
    return redirect("position", username=request.user.username, role=request.user.role)


def viewjob(request, job_id):
    job = Job.objects.get(id=job_id)
    return render(request, "userweb/view_job.html", {"job": job})

def view_company(request, company_name_eng):
    # ค้นหาข้อมูลของบริษัทในโมเดล CompanyInfo โดยใช้ company_name_eng
    company_info = get_object_or_404(CompanyInfo, company_name_eng=company_name_eng)

    # ค้นหา job ที่เชื่อมโยงกับบริษัทนี้
    jobs = Job.objects.filter(company=company_info)

    return render(request, "userweb/view_company.html", {"company_info": company_info, "jobs": jobs})

def viewalljob(request):
    jobs = Job.objects.all()
    return render(request, "userweb/jobs.html", {"jobs": jobs})

def applyjob(request, job_id):
    job = Job.objects.get(id=job_id)
    user = request.user
    student = StudentProfile.objects.get(user=user)
    student_info = student.studentinfo
    companyjob = CompanyProfile.objects.get(job=job_id)
    company_info = companyjob.companyinfo
    # company_name = job.company
    # company_profile = get_object_or_404(CompanyProfile, companyinfo__company_name_eng=company_name)
    # company_info = company_profile.companyinfo
    ststus = "Pending"
    matching = Matching.objects.create(student=student_info, job=job, company=company_info ,status=ststus)
    matching.save()
    messages.success(request, 'You have successfully applied for the job!')
    return redirect("view_job",job_id=job_id)


def viewselectcompany(request, role, username):
    student = StudentProfile.objects.get(user__username=username)
    match = Matching.objects.filter(student=student.studentinfo)
    job = [m.job for m in match]
    status = [m.status for m in match]
    showcompany = [m.company for m in match]
    interview = [m.interview for m in match]
    companies = zip(showcompany, status, job, interview)
    return render(request, "userweb/companyselect.html", {"company": companies})

def stdapproved(request, role, username):
    student = StudentProfile.objects.get(user__username=username)
    match = Matching.objects.filter(student=student.studentinfo)
    job = [m.job for m in match]
    status = [m.status for m in match]
    showcompany = [m.company for m in match]
    interview = [m.interview for m in match]
    companies = zip(showcompany, status, job, interview)
    return render(request, "stdstatus/approved.html", {"company": companies})

def stdrejected(request, role, username):
    student = StudentProfile.objects.get(user__username=username)
    match = Matching.objects.filter(student=student.studentinfo)
    job = [m.job for m in match]
    status = [m.status for m in match]
    showcompany = [m.company for m in match]
    interview = [m.interview for m in match]
    companies = zip(showcompany, status, job, interview)
    return render(request, "stdstatus/rejected.html", {"company": companies})

def stdinterviewed(request, role, username):
    student = StudentProfile.objects.get(user__username=username)
    match = Matching.objects.filter(student=student.studentinfo)
    job = [m.job for m in match]
    status = [m.status for m in match]
    showcompany = [m.company for m in match]
    interview = [m.interview for m in match]
    companies = zip(showcompany, status, job, interview)
    return render(request, "stdstatus/interview.html", {"company": companies})


def positionview(request, role, username):
    company_profile = CompanyProfile.objects.get(user__username=username)
    jobs = company_profile.job.all()
    return render(request, "userweb/position.html", {"jobs": jobs})


#บริษัทดูนิสิตที่สมัครงาน
def applyview(request, role, username):
    company = CompanyProfile.objects.get(user__username=username)
    match = Matching.objects.filter(company=company.companyinfo)
    match_id = [m.id for m in match]
    job = [m.job for m in match]
    status = [m.status for m in match]
    showstudent = [m.student for m in match]
    student_id = [s.student_id for s in showstudent]
    interview = [m.interview for m in match]
    students = zip(showstudent, status, job, match_id, student_id, interview)
    return render(request, "usertype/home_com.html", {"students": students, "role": role, "username": username})

def view_student(request, student_id):
    student = StudentInfo.objects.get(id=student_id)
    return render(request, "userweb/view_student.html", {"student": student})

def approvedview(request, role, username):
    company = CompanyProfile.objects.get(user__username=username)
    match = Matching.objects.filter(company=company.companyinfo)
    match_id = [m.id for m in match]
    job = [m.job for m in match]
    status = [m.status for m in match]
    showstudent = [m.student for m in match]
    student_id = [s.student_id for s in showstudent]
    interview = [m.interview for m in match]
    students = zip(showstudent, status, job, match_id, student_id, interview)
    return render(request, "status/approved.html", {"students": students, "role": role, "username": username})

def rejectedview(request, role, username):
    company = CompanyProfile.objects.get(user__username=username)
    match = Matching.objects.filter(company=company.companyinfo)
    match_id = [m.id for m in match]
    job = [m.job for m in match]
    status = [m.status for m in match]
    showstudent = [m.student for m in match]
    student_id = [s.student_id for s in showstudent]
    interview = [m.interview for m in match]
    students = zip(showstudent, status, job, match_id, student_id, interview)
    return render(request, "status/rejected.html", {"students": students, "role": role, "username": username})

def interviewedview(request, role, username):
    company = CompanyProfile.objects.get(user__username=username)
    match = Matching.objects.filter(company=company.companyinfo)
    match_id = [m.id for m in match]
    job = [m.job for m in match]
    status = [m.status for m in match]
    showstudent = [m.student for m in match]
    student_id = [s.student_id for s in showstudent]
    interview = [m.interview for m in match]
    students = zip(showstudent, status, job, match_id, student_id, interview)
    return render(request, "status/interview.html", {"students": students, "role": role, "username": username})

def approved(request, match_id):
    match = get_object_or_404(Matching, id=match_id)
    match.status = "Approved"
    match.save()
    messages.success(request, 'You have approved the student!')
    return redirect("studentview", role=request.user.role, username=request.user.username)

def interviewed(request, match_id):
    match = get_object_or_404(Matching, id=match_id)
    match.status = "Interview"
    match.save()
    messages.warning(request, 'You have selected the student for an interview!')
    return redirect("studentview", role=request.user.role, username=request.user.username)

def rejected(request, match_id):
    match = get_object_or_404(Matching, id=match_id)
    match.status = "Rejected"
    match.save()
    messages.error(request, 'You have rejected the student!')
    return redirect("studentview", role=request.user.role, username=request.user.username)

def inapproved(request, match_id):
    match = get_object_or_404(Matching, id=match_id)
    match.status = "Approved"
    match.save()
    messages.success(request, 'You have approved the student!')
    return redirect("interviewedview", role=request.user.role, username=request.user.username)

def inrejected(request, match_id):
    match = get_object_or_404(Matching, id=match_id)
    match.status = "Rejected"
    match.save()
    messages.error(request, 'You have rejected the student!')
    return redirect("interviewedview", role=request.user.role, username=request.user.username)

def addschedule(request, match_id):
    match = get_object_or_404(Matching, id=match_id)
    form = InterviewForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        date = form.cleaned_data["date"]
        time = form.cleaned_data["time"]
        location = form.cleaned_data["location"]
        link = form.cleaned_data["link"]
        interview = Interview.objects.create(date=date, time=time, location=location, link=link)
        interview.save()
        match.interview = interview
        match.save()
        messages.warning(request, 'You have successfully added the interview schedule!')
        return redirect("interviewedview", role=request.user.role, username=request.user.username)
    return render(request, "userweb/interviewform.html", {"form": form})

def search(request):
    if request.method == 'POST':
        form = JobSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            jobs = Job.objects.filter(Q(jobname__icontains=query) | Q(company__icontains=query))
            return render(request, 'usertype/search_results.html', {'jobs': jobs})
    else:
        form = JobSearchForm()
    return render(request, 'usertype/home.html', {'form': form})