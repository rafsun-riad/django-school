from rest_framework import serializers
from school.models import Class, Subject, Student, ClassSubject, Mark


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ClassSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassSubject
        fields = '__all__'


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'
