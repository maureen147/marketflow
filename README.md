MarketFlow - E-commerce API
A complete RESTful e-commerce backend API built with Django REST Framework.

Features
🔐 JWT Authentication

📦 Product management with categories

🛒 Shopping cart functionality

📊 Order processing

🔍 Product search and filtering

⭐ Product reviews and ratings

👑 Role-based permissions (Admin/Customer)

1. Clone and Setup
git clone https://github.com/maureen147/marketflow.git
cd marketflow
python -m venv venv

# Activate virtual environment
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

pip install -r requirements.txt

2. Database Setup

python manage.py migrate
python manage.py createsuperuser
# Follow prompts to create admin user

3. Run Server
python manage.py runserver
Visit: http://localhost:8000/

API Endpoints
Authentication
POST /api/token/ - Get JWT token

POST /api/token/refresh/ - Refresh token

Products
GET /api/products/ - List products (paginated)

POST /api/products/ - Create product (Admin only)

GET /api/products/{id}/ - Product details

GET /api/products/search/?q=keyword - Search products

Cart
GET /api/cart/ - View cart

POST /api/cart/add/ - Add to cart

POST /api/checkout/ - Create order

Orders
GET /api/orders/ - List orders

GET /api/orders/{id}/ - Order details

Test Users
Admin: glowworm / [your password]

Customer: customer@marketflow.com / customer123

Project Structure

marketflow/
├── products/     # Product management
├── orders/       # Cart and orders
├── users/        # Authentication
└── core/         # Django settings

Testing
python manage.py test

Technologies
Django & Django REST Framework

JWT Authentication

SQLite Database

django-filter for search/filtering

