from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Patientregistration(models.Model):
    username = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50,choices = (("male","Male"),("female","Female")))
    date_added =models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.username
    class Meta:
        ordering = ["-username"]

class Patientdata(models.Model):
    heart_rate = models.FloatField()
    spo2 = models.FloatField()
    blood_pressure = models.CharField(max_length=20)
    date_added =models.DateTimeField(default=datetime.now)
    patient = models.ForeignKey(Patientregistration,on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.username
