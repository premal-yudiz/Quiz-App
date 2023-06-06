from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    student_rollnum = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)
    marks = models.IntegerField(default=0)

    def __str__(self):
        return self.student_name
  
    

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=50)
    teacher_id = models.IntegerField(unique=True)
    password = models.CharField(max_length=50)    

    def __str__(self):
        return self.teacher_name
    

class QuesModel(models.Model):
    question = models.CharField(max_length=200)
    op1 = models.CharField(max_length=200)
    op2 = models.CharField(max_length=200)
    op3 = models.CharField(max_length=200)
    op4 = models.CharField(max_length=200)
    ans = models.CharField(max_length=200)
    
    def __str__(self):
        return self.question