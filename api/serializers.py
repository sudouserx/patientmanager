from rest_framework import serializers

from .models import HeartRate, Patient, User


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ("email", "password")

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists.")
        return value


class PatientSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(
        format="%Y-%m-%d",  # Output format
        input_formats=["%Y-%m-%d", "iso-8601"],  # Accepted input formats
    )

    class Meta:
        model = Patient
        fields = ("id", "first_name", "last_name", "date_of_birth", "created_at")
        read_only_fields = ("id", "created_at")


class HeartRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeartRate
        fields = ("id", "patient", "bpm", "timestamp")
        read_only_fields = ("id", "timestamp")
