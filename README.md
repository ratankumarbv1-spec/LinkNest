# 🔗 LinkNest

> Your personal library for the internet.

LinkNest is a full-stack Django web application that lets users save, organize, and manage their important links in one personal space.

Instead of keeping useful resources scattered across browser bookmarks, notes, messages, and different apps, LinkNest provides a simple centralized place to store everything worth remembering.

## 🌐 Live Demo

🚀 **[Visit LinkNest](https://linknest-aihk.onrender.com)**

## ✨ Features

- 🔐 User registration and login
- 👤 Individual user accounts and data
- 🔗 Add and save links
- ✏️ Edit saved links
- 🗑️ Delete links
- ⭐ Mark links as favourites
- 🏷️ Organize links using categories
- 🔎 Search through saved links
- 📊 Personal dashboard with link statistics
- 🚪 Secure logout
- 🔒 Password show/hide functionality
- 📱 Responsive interface
- 🌙 Modern dark-themed UI

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Django Authentication
- PostgreSQL

### Frontend
- HTML5
- CSS3
- JavaScript

### Database
- PostgreSQL
- SQLite for local development

### Deployment
- Render
- Gunicorn
- WhiteNoise

### Development Tools
- VS Code
- Git
- GitHub

## 🏗️ Project Structure

```text
LinkNest/
│
├── accounts/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── links/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── templates/
│   ├── base.html
│   ├── landing.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_link.html
│   ├── edit_link.html
│   ├── delete_link.html
│   └── profile.html
│
├── manage.py
├── requirements.txt
├── build.sh
└── render.yaml
