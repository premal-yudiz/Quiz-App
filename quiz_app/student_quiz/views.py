from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import *


def home(request):
    if request.method == "POST":
        option = request.POST.get('choice')
        print("optionn",option)
        if option == 'Teacher':
            return redirect('teacher_login')
        else:
            return redirect('student_login')

    return render(request,'home.html')

def teacher_registration(request):
    if request.method == "POST":
        name = request.POST['name']
        idd = request.POST['id']
        password = request.POST['password']
        rpt_password = request.POST['rpt_password']
        if password == rpt_password:
            try:    
                obj = Teacher(teacher_name=name, teacher_id=idd, password=password)
                print("objecttttt",obj)
                if obj:
                    obj.save()
                    return redirect('teacher_login')
            except Exception as e:
                return HttpResponse("Plese enter your Unique ID")
        else:
            return HttpResponse("Enter same password...")

    return render(request, 'teacher_registration.html')

def student_registration(request):
    if request.method == "POST":
        name = request.POST['name']
        roll_num = request.POST['roll_num']
        password = request.POST['password']
        rpt_password = request.POST['rpt_password']
        if password == rpt_password:
            try:
                    obj = Student(student_name=name, student_rollnum=roll_num, password=password)
                    print("objecttttt",obj)
                    if obj:
                        obj.save()
                        return redirect('student_login')
            except Exception as e:
                return HttpResponse("Enter your valid Enrollment number")
        else:
            return HttpResponse("enter same password...")
    return render(request, 'student_registration.html')
            

    
def student_login(request):
    if request.method == "POST":
        roll_num = request.POST.get('roll_num')
        request.session['student_login']= roll_num
        password = request.POST.get('password')
        try:
            obj = Student.objects.get(student_rollnum=roll_num)  
            if obj: 
                if obj.password==password:
                    return redirect('index_page')
                else:
                    return HttpResponse("password not match...")
            else:
                return HttpResponse("You are not registred user")
        except Exception as e:
            return HttpResponse("You are not registred user")
    
    return render(request,'student_login.html')    

def teacher_login(request):
    if request.method == "POST":
        tid = request.POST.get('teacher_id')
        print("name", tid)
        password = request.POST.get('password')
        print("pass", password)
        try:
            obj = Teacher.objects.get(teacher_id=tid)      
            if obj: 
                if obj.password==password:
                    request.session['teacher_login'] = tid

                    return redirect('teacher_index_page')
                else:
                    return HttpResponse("password not match...")
            else:
                return HttpResponse("You are not registred user")
        except Exception as e:
            return HttpResponse("You are not registred user")
    return render(request,'teacher_login.html')    
    

def index(request):
    if 'student_login' in request.session.keys():
        obj = Student.objects.get(student_rollnum = request.session['student_login'])
        context = {
            "obj": obj
        }
        return render(request,"index.html", context)
    
    else:
        return redirect('student_login')

def teacher_index(request):
    if 'teacher_login' in request.session.keys():
        student = Student.objects.all().order_by('-marks')
        context = {
            'student' : student
        }
        return render(request,"teacher_index.html",context)
    else:
        return redirect('teacher_login')
        
def logout(request):
    if 'teacher_login' in request.session.keys():
        request.session.pop('teacher_login')
        return redirect('home')
    elif 'student_login' in request.session.keys():
        request.session.pop('student_login')
        return redirect('home')

def question_test(request):
    if 'student_login' in request.session.keys():
        if request.method == 'POST':
            print(request.POST)
            questions=QuesModel.objects.all()
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                total+=1
                print(request.POST.get(q.question))
                print("answer is..",q.ans)
                print("type..",q.ans)
                print("type ans..",request.POST.get(q.question))
                if q.ans ==  request.POST.get(q.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            # percent = score/(total*10) *100
            context = {
                'score':score,
                'correct':correct,
                'time': request.POST.get('timer'),
                'wrong':wrong,
                # 'percent':percent,
                'total':total
            }
            obj = Student.objects.filter(student_rollnum=request.session['student_login']).update(marks=score)
            print("score is..",score)
            # obj.save()

            return render(request,'result.html',context)
        else:
            questions=QuesModel.objects.all()
            
            context = {
                
                'questions':questions
            }
            return render(request,'quiz.html',context)
    else:
        return redirect('student_login')
    
def add_question(request):
    if 'teacher_login' in request.session.keys():

        if request.method == "POST":
            question = request.POST.get('question')
            op1 = request.POST.get('op1')
            op2 = request.POST.get('op2')
            op3 = request.POST.get('op3')
            op4 = request.POST.get('op4')
            ans = request.POST.get('ans')
            obj = QuesModel(question=question,op1=op1,op2=op2,op3=op3,op4=op4,ans=ans) 
            if obj:
                obj.save()   
                return redirect('teacher_index_page')
        else:
            return render(request, 'add_question.html')
    else:
        return redirect('teacher_login')

def score_view(request):
    if 'student_login' in request.session.keys():

        obj = Student.objects.get(student_rollnum = request.session['student_login'])
        context = {
                "obj": obj
            }
        return render(request,'score_view.html',context)
    else:
        return redirect('student_login')




    