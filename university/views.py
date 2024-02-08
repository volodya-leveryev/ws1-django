from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from university import serializers
from university.models import Student, EduGroup


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    # permission_classes = [permissions.IsAuthenticated]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]


class EduGroupViewSet(viewsets.ModelViewSet):
    queryset = EduGroup.objects.all()
    serializer_class = serializers.EduGroupSerializer
    # permission_classes = [permissions.IsAuthenticated]
