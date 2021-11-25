from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SystemUserSerializer , TeacherSerializer , StudentSerializer
from .models import System_user 
# , Teacher, Student

# Create your views here.
@api_view()
def sample_url(request):
    return Response({"message": "Hello, world!"})

class CreateSystemUserView(APIView):
    
    def post(self,request):
        serializer = SystemUserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    # def get(self,request):
    #     userprofiles = System_user.objects.all()
    #     serializer = SystemUserSerializer(userprofiles)
    #     return Response(serializer.data)

class CreateTeacherView(APIView):
    
    def post(self,request):
        serializer = TeacherSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class CreateStudentView(APIView):
    
    def post(self,request):
        serializer = StudentSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)