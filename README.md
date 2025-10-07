# User Management System

A mini project built using **Django** that provides complete user management functionality. It allows users to register, log in, update their profiles, and perform administrative actions such as viewing, editing, and deleting user accounts.

---

## Features

* User registration with validation
* Secure authentication (login and logout)
* Profile view and update functionality
* Password hashing and reset support
* Django admin panel for user management
* Success and error notifications using the Django messages framework
* PostgreSQL database integration
* Secure environment variable configuration
* Clean, responsive UI using Django templates and Bootstrap

---

## Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Bootstrap
* **Database:** PostgreSQL
* **Environment Management:** python-dotenv
* **Version Control:** Git and GitHub

---

## Project Setup

Follow the steps below to set up and run the project locally.

### 1. Clone the Repository

```
git clone https://github.com/navaneethsankar07/User-Management-Django-.git
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # For Windows
# or
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File

Create a file named `.env` in the project root directory and add your environment variables:

```
SECRET_KEY=your_secret_key
DEBUG=True

# PostgreSQL Database Configuration
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Configure `settings.py` for PostgreSQL

Ensure your `DATABASES` configuration in `settings.py` looks like this:

```python
import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

```bash
python manage.py createsuperuser
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Now, open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## Folder Structure

```
user-management-system/
│
├── usermanagement/         # Main project directory (settings, urls, wsgi)
├── accounts/               # App handling user registration and login
├── templates/              # HTML templates
├── static/                 # Static files (CSS, JS, images)
├── .env                    # Environment variables (ignored by git)
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

---

## .gitignore Configuration

The `.gitignore` file ensures that sensitive and unnecessary files are not pushed to GitHub:

```
.env
__pycache__/
venv/
*.pyc
db.sqlite3
/staticfiles/
```

---

## Future Improvements

* Add email verification during registration
* Implement two-factor authentication
* Allow users to upload and update profile pictures
* Add pagination and search functionality for admin user management
* Write unit tests for critical components

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---
