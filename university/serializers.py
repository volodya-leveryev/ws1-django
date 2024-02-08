from django.contrib.auth.models import Group, User
from rest_framework import serializers

from university.models import Student, EduGroup


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['url', 'last_name', 'first_name', 'second_name', 'group']


class EduGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EduGroup
        fields = '__all__'
