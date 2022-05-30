from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        user_1=User.objects.get(username=user.username)
        user2=Teacher_Registration.objects.get(user=user)
        try:
            if user and user2.status=="Accept":
                login(request, user)
                return redirect('evolution')
            else:
                error ="yes"
        except:
            error = "yes"
    return render(request, 'login.html')

def register_view(request):
    if request.method=="POST":
        u = request.POST['name']
        c = request.POST['college']
        e = request.POST['email']
        p = request.POST['password']
        s = request.POST['stream']
        b = request.POST['branch']
        try:
            user = User.objects.create_user(username=u,password=p,email=e)
            Teacher_Registration.objects.create(user=user, college_id=c,status="pending",branch=b,stream=s)
            return redirect('login')
            error="no"
        except:
            error="yes"
    return render(request, 'register.html',locals())

def home(request):
    return render(request, 'home.html')

def pending_registration(request):
    teachers = Teacher_Registration.objects.filter(status = "pending")
    d = {'teachers':teachers}
    return render(request, 'pending.html',d)


def admin_home(request):
    return render(request, 'admin.html')


def assign_status(request,pid):
    
    teachers = Teacher_Registration.objects.get(id=pid)
    error = ""
    if request.method=='POST':
        s = request.POST['status']
        try:
            teachers.status = s
            teachers.save()
            error="no"
        except:
            error="yes"
    d = {'teachers':teachers,'error':error}
    return render(request, 'assign_status.html',d)

def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        if u=="admin" and p=="admin123#":
            return redirect('pending_notes')

    return render(request, 'admin_login.html',locals())

def evalution_page(request):
    return render(request,'evolution.html')

def Logout_view(request):
    logout(request)
    return redirect('home')

def studentdata(request):
    if request.method=="POST":
        u = request.POST['username']
        m = request.POST['marks']

        Student_Data.objects.create(studentname=u,marks=m)
        return redirect('home')

def student_marks(request):
    users=Student_Data.objects.all()
    d = {'users':users}
    return render(request,'view_users.html',d)

def teacher_details(request):
    teachers=Teacher_Registration.objects.all()
    d={'teachers':teachers}
    return render(request,'teacher_details.html',d)