from django.urls import path
from django.urls import path
from  .views import sample_url , CreateSystemUserView , CreateTeacherView , CreateStudentView

urlpatterns = [
    path('sample/',sample_url),
    path('users/',CreateSystemUserView.as_view()),
    path('teacher/',CreateTeacherView.as_view()),
    path('student/',CreateStudentView.as_view()),
    # .as_view()
]