from .models import Application
from .serializers import ApplicationSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets 


# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all().order_by('-id')
