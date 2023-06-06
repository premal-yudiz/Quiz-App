from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("registration-teacher", views.teacher_registration, name="teacher_registration"),
    path("registration-student", views.student_registration, name="student_registration"),
    path("student-login", views.student_login, name="student_login"),
    path("teacher-login", views.teacher_login, name="teacher_login"),
    path("index", views.index, name="index_page"),
    path("teacher_index", views.teacher_index, name="teacher_index_page"),
    path("question_test", views.question_test,name="question_test"),
    path("logout", views.logout,name="logout"),
    path("add_question", views.add_question,name="add_question"),
    path("score_view", views.score_view,name="score_view")
]