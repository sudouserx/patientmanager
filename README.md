# 🚑 PatientManager - Heart Rate Monitoring System

![Django](https://img.shields.io/badge/Django-4.2-brightgreen)
![DRF](https://img.shields.io/badge/DRF-3.14-blue)
![JWT](https://img.shields.io/badge/JWT-Auth-orange)
![Coverage](https://img.shields.io/badge/Coverage-93%25-green)

A robust **Django-based** patient management and heart rate monitoring system with REST API endpoints, JWT authentication, and comprehensive testing.

---

## ✨ Features

### 🔐 **User Authentication**
- **JWT-based authentication system** for secure access
- User registration & login endpoints
- Secure password handling with Django's built-in hashing
- Throttling for authentication endpoints to prevent abuse

### 🏥 **Patient Management**
- Create and manage patient profiles
- Store patient details (Name, DOB, and timestamps)
- User-specific patient data isolation for privacy
- RESTful API for CRUD operations

### ❤️ **Heart Rate Monitoring**
- Record & track patient heart rates with timestamps
- Patient-specific heart rate history retrieval
- Efficient database indexing for fast queries
- Data validation for heart rate values

### 🔌 **API Endpoints**
- RESTful API design following best practices
- JSON responses with proper HTTP status codes
- Comprehensive error handling for all endpoints
- Rate limiting for sensitive operations

### ✅ **Testing**
- Comprehensive unit and integration tests
- Test coverage reporting (93% coverage)
- Fixtures for consistent test data
- Database testing with SQLite

---

## 🛠 Technology Stack

- **Backend**: Django 4.2
- **API Framework**: Django REST Framework 3.14
- **Authentication**: Simple JWT
- **Database**: SQLite3 (Development), PostgreSQL (Production-ready)
- **Testing**: pytest with coverage reporting
- **Dependencies**: See `requirements.txt`

---

## 🚀 Installation Guide

### ✅ Prerequisites
- **Python 3.10+**
- **pip** (Python package manager)

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

6️⃣ **Create a superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7️⃣ **Run the development server**
   ```bash
   python manage.py runserver
   ```

8️⃣ **Access the API**
   - Visit `http://localhost:8000/api/v1/` in your browser or API client.

---

## 📡 API Documentation

### 🔑 Authentication
- **Register User** → `POST /api/v1/register/`
  - Required: `email`, `password`
  - Returns: User details

- **Login** → `POST /api/v1/login/`
  - Required: `email`, `password`
  - Returns: `access` and `refresh` tokens

### 🏥 Patient Management
- **Create Patient** → `POST /api/v1/patients/`
  - Required: `first_name`, `last_name`, `date_of_birth`
  - Authentication required

- **List Patients** → `GET /api/v1/patients/`
  - Returns: List of patients for the authenticated user

### ❤️ Heart Rate Monitoring
- **Record Heart Rate** → `POST /api/v1/heart-rate/`
  - Required: `patient_id`, `bpm`
  - Authentication required

- **Get Heart Rate History** → `GET /api/v1/heart-rate/?patient_id=<id>`
  - Returns: Heart rate history for a specific patient

---

## 🧪 Running Tests

To execute tests with coverage reporting:
```bash
pytest --cov=api --cov-report=term-missing
```

### 🔍 Test Coverage Includes:
- ✅ User registration & authentication
- ✅ Patient creation & management
- ✅ Heart rate recording & retrieval
- ✅ API endpoint validation
- ✅ Error handling for invalid requests

---

## 🤝 Contributing

We welcome contributions! Follow these steps:

1️⃣ Fork the repository  
2️⃣ Create a new branch: `git checkout -b feature/your-feature`  
3️⃣ Commit your changes: `git commit -am 'Add some feature'`  
4️⃣ Push to your branch: `git push origin feature/your-feature`  
5️⃣ Submit a Pull Request 🎉  

### Contribution Guidelines:
- Follow PEP 8 coding standards
- Write tests for new features
- Update documentation as needed
- Use descriptive commit messages

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