from rest_framework import serializers
from .models import System_user , Teacher, Student

class SystemUserSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True),
    users_name =serializers.CharField(),
    users_age =serializers.IntegerField(),
    gender =serializers.CharField(),
    role =serializers.CharField()

    def create(self,validated_data):
        return System_user.objects.create(**validated_data)
   
    def update(self,instance,validated_data):
        instance.users_name =validated_data.get('users_name',instance.users_name)
        instance.users_age =validated_data.get('users_age',instance.users_age)
        instance.gender =validated_data.get('gender',instance.gender)
        instance.role =validated_data.get('role',instance.role)
        instance.save()

        return instance

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Student
        fields = '__all__'