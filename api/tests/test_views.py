import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from ..models import HeartRate, Patient, User


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
    data = {"email": "new@example.com", "password": "SecurePass123"}
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert User.objects.filter(email="new@example.com").exists()


@pytest.mark.django_db
def test_duplicate_registration(api_client, test_user):
    url = reverse("register")
    data = {"email": "test@example.com", "password": "testpass123"}
    response = api_client.post(url, data)
    assert response.status_code == 400
    assert "user with this email already exists." in str(response.content)


@pytest.mark.django_db
def test_valid_login(api_client, test_user):
    url = reverse("login")
    data = {"email": "test@example.com", "password": "testpass123"}
    response = api_client.post(url, data)
    assert response.status_code == 200
    assert "access" in response.data


@pytest.mark.django_db
def test_invalid_login(api_client, test_user):
    url = reverse("login")
    data = {"email": "test@example.com", "password": "wrongpass"}
    response = api_client.post(url, data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_unauthenticated_patient_access(api_client):
    url = reverse("patients")
    response = api_client.get(url)
    assert response.status_code == 401


@pytest.mark.django_db
def test_patient_creation(authenticated_client):
    url = reverse("patients")
    data = {"first_name": "Jane", "last_name": "Smith", "date_of_birth": "1999-12-31"}
    response = authenticated_client.post(url, data)
    assert response.status_code == 201
    assert Patient.objects.filter(first_name="Jane").exists()


@pytest.mark.django_db
def test_invalid_patient_data(authenticated_client):
    url = reverse("patients")
    data = {"first_name": "", "last_name": "Doe", "date_of_birth": "invalid-date"}
    response = authenticated_client.post(url, data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_heart_rate_creation(authenticated_client, test_patient):
    url = reverse("heart-rate")
    data = {"patient_id": test_patient.id, "bpm": 85}
    response = authenticated_client.post(url, data)
    assert response.status_code == 201
    assert HeartRate.objects.filter(bpm=85).exists()


@pytest.mark.django_db
def test_heart_rate_invalid_data(authenticated_client, test_patient):
    url = reverse("heart-rate")
    # Missing patient_id
    response = authenticated_client.post(url, {"bpm": 85})
    assert response.status_code == 400
    # Invalid BPM type
    response = authenticated_client.post(
        url, {"patient_id": test_patient.id, "bpm": "eighty"}
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_heart_rate_list(authenticated_client, test_patient):
    HeartRate.objects.create(patient=test_patient, bpm=72)
    url = reverse("heart-rate") + f"?patient_id={test_patient.id}"
    response = authenticated_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["bpm"] == 72


@pytest.mark.django_db
def test_nonexistent_patient_heart_rate(authenticated_client):
    url = reverse("heart-rate") + "?patient_id=999"
    response = authenticated_client.get(url)
    assert response.status_code == 404
