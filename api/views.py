from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, ProjectSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Project
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer


class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.kwargs['username']
        user = User.objects.get(username=user)
        return Project.objects.filter(user=user).order_by('-created_at')


class ProjectCreate(generics.CreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)


class ProjectDetail(generics.RetrieveAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Project.objects.filter(id=pk)


class ProjectUpdate(generics.UpdateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ProjectDelete(generics.DestroyAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(user=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
