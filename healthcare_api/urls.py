# healthcare_api/urls.py

from django.urls import path
from .views import (
    RegisterView,
    LoginView,
    PatientListCreateView,
    PatientDetailView,
    DoctorListCreateView,
    DoctorDetailView,
    PatientDoctorMappingListCreateView,
    PatientDoctorMappingDetailView,
    PatientDoctorsListView,
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    # Register path.
    path('auth/register/', RegisterView.as_view(), name='register'),
    # Login path.
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Patient saving details or fetching details path.
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    # To see specific patient details with id, path.
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),

    # Doctor saving details or fetching details path.
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    # To see specific doctor details with id, path.
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),

    # Mappings to assign doctor to patient.
    path('mappings/', PatientDoctorMappingListCreateView.as_view(), name='mapping-list-create'),
    path('mappings/<int:patient_id>/', PatientDoctorsListView.as_view(), name='patient-doctors-list'),
    path('mappings/detail/<int:pk>/', PatientDoctorMappingDetailView.as_view(), name='mapping-detail'),
]