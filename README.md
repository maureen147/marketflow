🛒 MarketFlow – E-commerce REST API

MarketFlow is a RESTful e-commerce backend built with Django REST Framework.
It provides all core features needed to power an online store, including authentication, product management, shopping cart, orders, and reviews.

🚀 Key Features

🔐 JWT Authentication – Secure login and access control

🛍️ Product Management – Create, view, update, and delete products & categories

🛒 Shopping Cart – Add, update, and remove cart items

📦 Order Processing – Checkout, order tracking, and status updates

⭐ Product Reviews – User ratings and comments

🔍 Search & Filters – Search by name, category, price, and availability

📱 Pagination – Efficient loading of large product lists

👑 Admin Dashboard – Manage products and orders via Django Admin

🔒 Role-Based Permissions – Admin vs customer access

🛠️ Tech Stack

Backend: Django, Django REST Framework

Authentication: JWT

Database: SQLite (development)

Tools: Postman, Git, Render (deployment)

⚙️ Setup (Quick Start)
git clone https://github.com/yourusername/marketflow.git
cd marketflow
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


Access API at: http://127.0.0.1:8000/

🔐 Authentication

Get token: POST /api/token/

Register user: POST /api/register/

Use token in headers:

Authorization: Bearer <access_token>

📦 Core Endpoints
Products

GET /api/products/ – List products

GET /api/products/{id}/ – Single product

POST /api/products/ – Create product (Admin)

Cart

GET /api/cart/ – View cart

POST /api/cart/add/ – Add item

PUT /api/cart/items/{id}/ – Update item

DELETE /api/cart/items/{id}/remove/ – Remove item

Orders

POST /api/checkout/ – Place order

GET /api/orders/ – View orders

Reviews

GET /api/products/{id}/reviews/

POST /api/products/{id}/reviews/

🧪 Testing

Run tests:

python manage.py test


Test APIs using Postman or curl

🛡️ Security

JWT-based authentication

Input validation

Django ORM protection against SQL injection

Role-based access control

🚀 Deployment

Deployed using Render with:

gunicorn core.wsgi:application

Environment variables for SECRET_KEY, DEBUG, and settings