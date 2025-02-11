import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from ..models import User, Patient, HeartRate
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user():
    return User.objects.create_user(email="test@example.com", password="testpass123")

@pytest.fixture
def test_patient(test_user):
    return Patient.objects.create(
        user=test_user,
        first_name="John",
        last_name="Doe",
        date_of_birth="2000-01-01",
    )

@pytest.fixture
def authenticated_client(api_client, test_user):
    refresh = RefreshToken.for_user(test_user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")
    return api_client

@pytest.mark.django_db
def test_user_registration(api_client):
    url = reverse("register")
    data = {"email": "newuser@example.com", "password": "newpass123"}
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert User.objects.filter(email="newuser@example.com").exists()

@pytest.mark.django_db
def test_user_login(api_client, test_user):
    url = reverse("login")
    data = {"email": "test@example.com", "password": "testpass123"}
    response = api_client.post(url, data)
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_patient_creation(authenticated_client, test_user):
    url = reverse("patients")
    data = {
        "first_name": "Jane",
        "last_name": "Doe",
        "date_of_birth": "1995-05-05",
    }
    response = authenticated_client.post(url, data)
    assert response.status_code == 201
    assert Patient.objects.filter(first_name="Jane", user=test_user).exists()

@pytest.mark.django_db
def test_heart_rate_creation(authenticated_client, test_patient):
    url = reverse("heart-rate")
    data = {
        "patient_id": test_patient.id,
        "bpm": 80,
    }
    response = authenticated_client.post(url, data)
    assert response.status_code == 201
    assert HeartRate.objects.filter(patient=test_patient, bpm=80).exists()

@pytest.mark.django_db
def test_heart_rate_list(authenticated_client, test_patient):
    HeartRate.objects.create(patient=test_patient, bpm=72)
    url = reverse("heart-rate") + f"?patient_id={test_patient.id}"
    response = authenticated_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["bpm"] == 72