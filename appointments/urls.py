from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_prescription, name='add_prescription'),
]

urlpatterns = [
    path('add/', views.add_prescription, name='add_prescription'),
    path('my-prescriptions/', views.patient_prescriptions, name='patient_prescriptions'),
]
