from django.urls import path
from .views import UserRegistrationView, UserLoginView, PatientView, HeartRateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('patients/', PatientView.as_view()),
    path('heart-rate/', HeartRateView.as_view()),
]