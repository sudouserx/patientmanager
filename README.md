# 🚑 PatientManager - Heart Rate Monitoring System

![Django](https://img.shields.io/badge/Django-4.2-brightgreen)
![DRF](https://img.shields.io/badge/DRF-3.14-blue)
![JWT](https://img.shields.io/badge/JWT-Auth-orange)

A robust **Django-based** patient management and heart rate monitoring system with REST API endpoints, JWT authentication, and comprehensive testing.

---

## ✨ Features

### 🔐 **User Authentication**
- JWT-based authentication system
- User registration & login endpoints
- Secure password handling
- Throttling for authentication endpoints

### 🏥 **Patient Management**
- Create and manage patient profiles
- Store patient details (Name, DOB)
- User-specific patient data isolation

### ❤️ **Heart Rate Monitoring**
- Record & track patient heart rates
- Timestamped heart rate data
- Patient-specific heart rate history
- Efficient database indexing for performance

### 🔌 **API Endpoints**
- RESTful API design
- JSON responses with proper status codes
- Error handling & rate limiting for sensitive endpoints

### ✅ **Testing**
- Comprehensive unit tests
- Integration tests for API endpoints
- Fixtures for test data
- Database testing support

---

## 🛠 Technology Stack

- **Backend**: Django 4.2
- **API Framework**: Django REST Framework 3.14
- **Authentication**: JWT (Simple JWT)
- **Database**: SQLite3
- **Testing**: pytest

---

## 🚀 Installation Guide

### ✅ Prerequisites
- **Python 3.10+** installed

### 🔧 Setup Instructions

1️⃣ **Clone the repository**
   ```bash
   git clone https://github.com/sudouserx/patientmanager.git
   cd patientmanager
   ```

2️⃣ **Create & activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3️⃣ **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4️⃣ **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your database credentials
   ```

5️⃣ **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6️⃣ **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7️⃣ **Start the development server**
   ```bash
   python manage.py runserver
   ```

---

## 📡 API Documentation

### 🔑 Authentication
- **Register User** → `POST /api/v1/register/`
  - Required: `email`, `password`

- **Login** → `POST /api/v1/login/`
  - Required: `email`, `password`
  - Returns: `access` and `refresh` tokens

### 🏥 Patient Management
- **Create Patient** → `POST /api/v1/patients/`
  - Required: `first_name`, `last_name`, `date_of_birth`
  - Authentication required

- **List Patients** → `GET /api/v1/patients/`
  - Returns patient list for authenticated user

### ❤️ Heart Rate Monitoring
- **Record Heart Rate** → `POST /api/v1/heart-rate/`
  - Required: `patient_id`, `bpm`
  - Authentication required

- **Get Heart Rate History** → `GET /api/v1/heart-rate/?patient_id=<id>`
  - Returns heart rate history for a patient

---

## 🧪 Running Tests

To execute tests, run:
```bash
pytest --cov=api --cov-report=term-missing
```

### 🔍 Test Coverage Includes:
✅ User registration & authentication
✅ Patient creation & management
✅ Heart rate recording & retrieval
✅ API endpoint validation
✅ Error handling

---

## 🤝 Contributing

We welcome contributions! Follow these steps:

1️⃣ Fork the repository
2️⃣ Create a new branch: `git checkout -b feature/your-feature`
3️⃣ Commit your changes: `git commit -am 'Add some feature'`
4️⃣ Push to your branch: `git push origin feature/your-feature`
5️⃣ Submit a Pull Request 🎉

💡 **Ensure your code follows PEP 8 guidelines & includes tests.**

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For inquiries or support, reach out via:

- **Project Maintainer**: SudouserX
- **Email**: ebrahimaliyou@gmail.com
- **Issue Tracker**: [GitHub Issues](https://github.com/sudouserx/patientmanager/issues)

🚀 **Happy Coding!**

