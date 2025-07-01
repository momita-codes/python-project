# SecureAuth-Django

-  A custom user authentication system built with Django and MySQL.
-  Includes secure login, registration with password confirmation, CSRF protection, error handling, and clean UI design using Bootstrap.
-  Includes username/email validation, error handling, and modern HTML templates styled with Bootstrap.

---

## 🚀 Features

- ✅ User Signup with password confirmation
- ✅ User Login & Logout
- ✅ CSRF protection
- ✅ Password hashing
- ✅ Error messages for duplicates & mismatches
- ✅ Clean UI with Bootstrap
- ✅ Fully working custom views (no Django auth forms)

---

## ⚙️ Tech Stack

- Python 3.x
- Django 5.x
- MySQL
- HTML5 + CSS3 + Bootstrap
- VS Code

---

## 📂 Project Structure

SecureAuth-Django/
├── SecureAuth/                         # 🔧 Main Django project folder
│   ├── __init__.py
│   ├── settings.py                     # Django project settings (DB config, templates, etc.)
│   ├── urls.py                         # Root URL configuration
│   └── wsgi.py                         # For deployment (used by web servers)
│   └── asgi.py
│
├── userauth/                           # 🔐 Custom Django app for authentication
│   ├── __init__.py
│   ├── views.py                        # Contains login, signup, logout logic
│   ├── urls.py                         # URLs for login, signup, etc.
│   ├── models.py                       # Extend if you want custom user fields
│   └── templates/
│           ├── login.html
│           ├── signup.html
│           ├── dashboard.html
│           └── edit_profile.html
│           └── base.html               # Used as a common layout with {% block %} tags
│   
├── static/                             # 🎨 CSS, JS, images (optional if you're adding styling)
│   └── css/
│       └── style.css                   # Your custom CSS
│
├── manage.py                           # Django's main command-line utility
├── db.sqlite3                          # Optional (if you’re using SQLite instead of MySQL)
├── README.md                           # 📘 Project overview and instructions
