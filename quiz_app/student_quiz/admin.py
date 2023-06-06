from django.contrib import admin
from .models import *
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'student_rollnum','password']
admin.site.register(Student, StudentAdmin)
class TeacherAdmin(admin.ModelAdmin):
    list_display =['teacher_name', 'teacher_id','password']
admin.site.register(Teacher,TeacherAdmin)    
class QuestionAdmin(admin.ModelAdmin):
    list_display =['question']
admin.site.register(QuesModel,QuestionAdmin)    
