from django.shortcuts import render
from rest_framework import viewsets
from doctorapp.serializers import DoctorSerializer,PatientSerializer
from doctorapp.models import doctor,patient


# Create your views here.

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = PatientSerializer