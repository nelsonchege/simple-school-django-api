from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import SystemUserSerializer , TeacherSerializer , StudentSerializer
from .models import System_user 
# , Teacher, Student

# Create your views here.
@api_view()
def sample_url(request):
    return Response({"message": "Hello, world!"})


@api_view(['GET','POST'])
def SystemUser(request):
    if request.method == 'GET':
        systemUser= System_user.objects.all()
        serializer =SystemUserSerializer(systemUser, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer =SystemUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message':'unable to save'},status=status.HTTP_424_FAILED_DEPENDENCY)


@api_view(['GET','PUT','DELETE'])
def UpdateSystemUser(request,pk):
    if request.method == 'GET':
        systemUser= System_user.objects.get(pk=pk)
        serializer =SystemUserSerializer(systemUser)
        return Response(serializer.data)
    if request.method == 'PUT':
        systemUser= System_user.objects.get(pk=pk)
        serializer =SystemUserSerializer(systemUser,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'message':'unable to save'},status=status.HTTP_424_FAILED_DEPENDENCY)
    if request.method == 'DELETE':
        systemUser= System_user.objects.get(pk=pk)
        systemUser.delete()
        return Response({'deleted successfully'})


# class CreateSystemUserView(APIView):
    
#     def post(self,request):
#         serializer = SystemUserSerializer(data = request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     def get(self,request):
#         userprofiles = System_user.objects.all()
#         serializer = SystemUserSerializer(userprofiles)
#         return Response(serializer.data)

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