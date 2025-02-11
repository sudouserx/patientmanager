import pytest
from django.utils import timezone
from ..models import User, Patient, HeartRate

@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(email="test@example.com", password="testpass123")
    assert user.email == "test@example.com"
    assert user.check_password("testpass123") is True

@pytest.mark.django_db
def test_patient_creation():
    user = User.objects.create(email="test@example.com", password="testpass123")
    patient = Patient.objects.create(
        user=user,
        first_name="John",
        last_name="Doe",
        date_of_birth=timezone.now().date(),
    )
    assert patient.first_name == "John"
    assert patient.last_name == "Doe"
    assert patient.user == user

@pytest.mark.django_db
def test_heart_rate_creation():
    user = User.objects.create(email="test@example.com", password="testpass123")
    patient = Patient.objects.create(
        user=user,
        first_name="John",
        last_name="Doe",
        date_of_birth=timezone.now().date(),
    )
    heart_rate = HeartRate.objects.create(patient=patient, bpm=72)
    assert heart_rate.patient == patient
    assert heart_rate.bpm == 72