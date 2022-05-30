"""QR_code URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from qr_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.login_view,name="login"),
    path('register/',views.register_view,name="register"),
    path('admin_home/',views.admin_home,name="admin_home"),
    path('pending_registrtion/',views.pending_registration,name="pending_notes"),
    path('assign_status/<int:pid>',views.assign_status, name='assign_status'),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('evolution/',views.evalution_page,name="evolution"),
    path('logout/',views.Logout_view,name="logout"),
    path('studentdata/',views.studentdata,name="studentdata"),
    path('student_marks/',views.student_marks,name="student_marks"),
    path('teacher_details/',views.teacher_details,name="teacher_details")
]
