# 📝 Django REST Blog API

A simple blog backend built with **Django** and **Django REST Framework**, ready to connect with any frontend (React, etc.).

## ✅ Features

- JWT Authentication (register/login/refresh)
- Custom User Model
- CRUD for Blog Posts with Image Upload
- Category Management
- Comments with nested replies
- Like/Unlike comments
- Slug-based URLs for posts
- Pagination & search support

---

## 🚀 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/yourusername/django-blog-api.git
cd django-blog-api

# Setup virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Migrate and create superuser
python manage.py migrate
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

---

## 🔐 Authentication

### Register

```
POST /api/users/register/
```

```json
{
  "username": "john",
  "email": "john@example.com",
  "password": "secret123"
}
```

### Login

```
POST /api/users/login/
```

```json
{
  "email": "john@example.com",
  "password": "secret123"
}
```

### Refresh Token

```
POST /api/users/refresh/
```

```json
{
  "refresh": "<refresh_token>"
}
```

> 🔑 Use the returned `access` token in the header:  
> `Authorization: Bearer <access_token>`

---

## 🗂️ Categories

### List Categories

```
GET /api/blog/categories/
```

### Create Category

```
POST /api/blog/categories/
```

```json
{
  "name": "Tech"
}
```

---

## 📝 Blog Posts

### List Posts (with pagination, search)

```
GET /api/blog/posts/
GET /api/blog/posts/?search=react
```

### Retrieve Post by Slug

```
GET /api/blog/posts/<slug>/
```

### Create Post

```
POST /api/blog/posts/
Headers: Authorization + multipart/form-data
```

**Form Data:**

```
title: My First Post
content: This is the content
category: 1
image: (select image file)
```

### Update Post

```
PUT /api/blog/posts/<slug>/
```

### Delete Post

```
DELETE /api/blog/posts/<slug>/
```

---

## 💬 Comments

### List Comments

```
GET /api/blog/comments/
GET /api/blog/comments/?post=1
```

### Create Comment

```
POST /api/blog/comments/
Headers: Authorization
```

```json
{
  "post": 1,
  "content": "Nice post!"
}
```

### Like/Unlike Comment

```
POST /api/blog/comments/<id>/like/
```

---

## 🌐 Admin Panel

```
http://127.0.0.1:8000/admin/
```

---

## 📁 Tech Stack

- Django 5.x
- Django REST Framework
- Simple JWT
- SQLite (for development)
- Pillow (for image upload)

---

## 📌 Coming Soon

- Author profile endpoint
- Post bookmarks
- Email notifications (optional)
- Frontend in React!

---

## 🧑‍💻 Author

**Sharan Panthi**  
MERN + Next.js Developer  
Feel free to connect!
