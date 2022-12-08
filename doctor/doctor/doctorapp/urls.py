from django.urls import include,path
from rest_framework import routers
from doctorapp.views import DoctorViewSet,PatientViewSet

router = routers.DefaultRouter()
router.register(r'doctor',DoctorViewSet)
router.register(r'patient',PatientViewSet)

urlpatterns = [
    path('',include(router.urls)),
]