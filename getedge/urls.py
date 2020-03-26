from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Patientsregistration',views.PatientregistrationViewSet)
router.register(r'Patientdata',views.PatientdataViewSet)

#wire up our API using automatic URL routing

#Adiitionally , we include URLs for the browsable API.

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]
