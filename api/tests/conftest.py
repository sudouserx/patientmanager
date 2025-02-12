import pytest
from django.contrib.auth import get_user_model

from api.models import Patient

User = get_user_model()


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
