# 📚 CrudAPI – Django REST Framework

A simple REST API built with Django and Django REST Framework that supports full CRUD (Create, Read, Update, Delete) operations on a `Book` resource.

This project is ideal for beginners learning RESTful APIs with Python and Django.

---

## 🚀 Features

- Add, retrieve, update, and delete books
- JSON-based API responses
- Organized code structure using DRF's views, serializers, and models
- Easily extendable for new models/resources

---

## 🛠️ Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (default)
- Git

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/dioramashvili/CrudAPI.git
cd CrudAPI

# Create virtual environment
python -m venv venv
source venv/bin/activate   # or venv\\Scripts\\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
