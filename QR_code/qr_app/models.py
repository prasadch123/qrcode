from django.db import models
from django.contrib.auth.models import User

class Teacher_Registration(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    college_id=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    stream=models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

class Student_Data(models.Model):
    studentname=models.CharField(max_length=50)
    marks=models.CharField(max_length=50)
    

