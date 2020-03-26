from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientregistrationSerializer
from .models import Patientregistration
from .models import Patientdata
from .serializers import PatientdataSerializer
# Create your views here.

class PatientregistrationViewSet(viewsets.ModelViewSet):
    queryset = Patientregistration.objects.all().order_by('username')
    serializer_class = PatientregistrationSerializer

class PatientdataViewSet(viewsets.ModelViewSet):
    queryset = Patientdata.objects.all().order_by('patient')
    serializer_class = PatientdataSerializer