from rest_framework import serializers
from .models import Patientregistration
from .models import Patientdata

class PatientregistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patientregistration
        fields = ('username','name','email','height','weight','age','gender','date_added')

class PatientdataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patientdata
        fields = ('heart_rate','spo2','blood_pressure','date_added','patient')
