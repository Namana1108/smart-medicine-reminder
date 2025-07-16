# appointments/forms.py
from django import forms
from .models import Prescription
from django.contrib.auth import get_user_model

User = get_user_model()

class PrescriptionForm(forms.ModelForm):
    patient = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Prescription
        fields = ['patient', 'medicine_name', 'dosage', 'time', 'instructions', 'phone_number']

    def __init__(self, *args, **kwargs):
        self.doctor = kwargs.pop('doctor', None)
        super().__init__(*args, **kwargs)
        if self.doctor:
            self.fields['patient'].queryset = User.objects.exclude(id=self.doctor.id)
