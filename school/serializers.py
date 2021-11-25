from rest_framework import serializers
from .models import System_user , Teacher, Student

class SystemUserSerializer(serializers.ModelSerializer):

    class Meta:
        model  = System_user
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Student
        fields = '__all__'