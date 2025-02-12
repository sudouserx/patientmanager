import pytest
from django.db import IntegrityError

from api.models import HeartRate, Patient, User


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create_user(email="test@example.com", password="testpass123")
    assert user.email == "test@example.com"


@pytest.mark.django_db
def test_user_email_uniqueness():
    User.objects.create_user(email="test@example.com", password="testpass123")
    with pytest.raises(IntegrityError):
        User.objects.create_user(email="test@example.com", password="anotherpass123")


@pytest.mark.django_db
def test_patient_creation(test_user):  # Uses test_user fixture
    patient = Patient.objects.create(
        user=test_user,
        first_name="John",
        last_name="Doe",
        date_of_birth="2000-01-01",
    )
    assert patient.user == test_user


@pytest.mark.django_db
def test_patient_cascade_on_user_delete(test_user):
    patient = Patient.objects.create(
        user=test_user, first_name="John", last_name="Doe", date_of_birth="2000-01-01"
    )
    test_user.delete()
    assert not Patient.objects.filter(id=patient.id).exists()


@pytest.mark.django_db
def test_heart_rate_creation(test_patient):  # Uses test_patient fixture
    heart_rate = HeartRate.objects.create(patient=test_patient, bpm=72)
    assert heart_rate.patient == test_patient


@pytest.mark.django_db
def test_heart_rate_cascade_on_patient_delete(test_patient):
    HeartRate.objects.create(patient=test_patient, bpm=72)
    test_patient.delete()
    assert not HeartRate.objects.exists()
