from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PrescriptionForm
from .send_sms import send_sms  # Add this import

# appointments/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PrescriptionForm
from .send_sms import send_sms  # ✅

@login_required
def add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, doctor=request.user)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = request.user
            prescription.save()

            # ✅ Send SMS
            phone = prescription.phone_number
            msg = f"💊 Reminder: Take {prescription.medicine_name} at {prescription.time.strftime('%I:%M %p')}."
            send_sms(phone, msg)

            return redirect('add_prescription')
    else:
        form = PrescriptionForm(doctor=request.user)

    return render(request, 'appointments/add_prescription.html', {'form': form})


from .models import Prescription

@login_required
def patient_prescriptions(request):
    prescriptions = Prescription.objects.filter(patient=request.user).order_by('-date_prescribed')
    return render(request, 'appointments/patient_prescriptions.html', {'prescriptions': prescriptions})
