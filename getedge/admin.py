from django.contrib import admin
from .models import Patientregistration
from .models import Patientdata
# Register your models here.

admin.site.register(Patientregistration)
admin.site.register(Patientdata)