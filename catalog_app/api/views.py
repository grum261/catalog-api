from .models import Applicant
from .serializers import ApplicantSerializer
from .permissions import IsOwner
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets


# Create your views here.
class ApplicantViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, IsOwner)
    serializer_class = ApplicantSerializer
    queryset = Applicant.objects.all().order_by('-id')