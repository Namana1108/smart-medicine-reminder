from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, DoctorProfile

class DoctorSignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    specialization = forms.CharField(max_length=100)
    experience = forms.IntegerField()
    contact_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_doctor = True
        if commit:
            user.save()
            DoctorProfile.objects.create(
                user=user,
                specialization=self.cleaned_data['specialization'],
                experience=self.cleaned_data['experience'],
                contact_number=self.cleaned_data['contact_number']
            )
        return user
