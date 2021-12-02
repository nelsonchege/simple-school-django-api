from django.urls import path
from django.urls import path
from  .views import sample_url , CreateTeacherView , CreateStudentView,UpdateSystemUser,SystemUser
# , CreateSystemUserView 
urlpatterns = [
    path('sample/',sample_url),
    path('teacher/',CreateTeacherView.as_view()),
    path('student/',CreateStudentView.as_view()),
    path('users/',SystemUser),
    path('users/<int:pk>',UpdateSystemUser),
    #  path('users/',CreateSystemUserView.as_view()),
    # .as_view()
]