# appointments/models.py
from django.db import models
from django.conf import settings

class Prescription(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_prescriptions')
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient_prescriptions')
    medicine_name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    time = models.TimeField()
    instructions = models.TextField(blank=True)
    date_prescribed = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, help_text='Enter in format +91XXXXXXXXXX')

    def __str__(self):
        return f"{self.medicine_name} for {self.patient.username}"
