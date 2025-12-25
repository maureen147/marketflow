<!-- 🛒 MarketFlow - E-commerce REST API -->
MarketFlow is a complete RESTful e-commerce backend API built with Django REST Framework. This API powers online shopping functionality with user authentication, product management, shopping cart, order processing, and reviews.

 <!-- Features -->
 JWT Authentication - Secure token-based authentication for users

🛍️ Product Management - Full CRUD operations for products and categories

🛒 Shopping Cart - Add, remove, and update items in cart

📦 Order Processing - Checkout, order tracking, and status management

⭐ Product Reviews - User ratings and comments system

🔍 Advanced Search - Filter products by category, price range, and availability

📱 Pagination - Efficient data loading with page-based results

👑 Admin Dashboard - Django admin panel for product management

🔒 Role-based Permissions - Admin vs customer access control


<!-- Prerequisites -->
Python 3.12+

pip (Python package manager)

<!-- Installation -->
Clone the repository

git clone https://github.com/yourusername/marketflow.git
cd marketflow

<!-- Create virtual environment -->
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

<!-- Install dependencies -->
pip install -r requirements.txt

<!-- Run migrations -->
python manage.py migrate

<!-- Create admin user and test data -->
python create_admin.py
python create_test_data.py

<!-- Start development server -->
python manage.py runserver

Visit http://127.0.0.1:8000/ to see the API homepage.

Authentication
All authenticated endpoints require JWT token in the header:

Authorization: Bearer <your_access_token>

<!-- Get Access Token -->
POST /api/token/
Content-Type: application/json

{
  "email": "customer@marketflow.com",
  "password": "customer123"
}

<!-- Register new user  -->
POST /api/register/
Content-Type: application/json

{
  "email": "newuser@example.com",
  "username": "newuser",
  "password": "securepassword123",
  "password2": "securepassword123"
}

📦 Products
<!-- List All Products -->
GET /api/products/

<!-- Search Products -->
GET /api/products/search/?q=laptop

<!-- Filter Products -->
GET /api/products/?category=1&min_price=100&max_price=1000&in_stock=true

<!-- Get Single Product -->
GET /api/products/{id}/

<!-- Create Product (Admin Only) -->
POST /api/products/
Authorization: Bearer <admin_token>

{
  "name": "New Product",
  "description": "Product description",
  "price": "99.99",
  "stock_quantity": 50,
  "category_id": 1
}

🛒 Cart Management
View Cart
http
GET /api/cart/
Authorization: Bearer <token>
Add to Cart
http
POST /api/cart/add/
Authorization: Bearer <token>

{
  "product_id": 1,
  "quantity": 2
}
Update Cart Item
http
PUT /api/cart/items/{item_id}/
Authorization: Bearer <token>

{
  "quantity": 3
}
Remove from Cart
http
DELETE /api/cart/items/{item_id}/remove/
Authorization: Bearer <token>
📋 Orders
Checkout
http
POST /api/checkout/
Authorization: Bearer <token>

{
  "shipping_address": "123 Main St, City, Country"
}
List Orders
http
GET /api/orders/
Authorization: Bearer <token>
Get Order Details
http
GET /api/orders/{id}/
Authorization: Bearer <token>
⭐ Reviews
Get Product Reviews
http
GET /api/products/{product_id}/reviews/
Add Review
http
POST /api/products/{product_id}/reviews/
Authorization: Bearer <token>

{
  "rating": 5,
  "comment": "Excellent product!"
}
📂 Categories
List Categories
http
GET /api/categories/
Create Category (Admin Only)
http
POST /api/categories/
Authorization: Bearer <admin_token>

{
  "name": "New Category",
  "description": "Category description"
}
🔧 Project Structure
text
marketflow/
├── core/                    # Django project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # URL routing
│   └── wsgi.py             # WSGI configuration
├── products/               # Products app
│   ├── models.py          # Product, Category, Review models
│   ├── views.py           # Product-related views
│   ├── serializers.py     # Product serializers
│   ├── urls.py            # Product endpoints
│   └── admin.py           # Admin configuration
├── orders/                 # Orders app
│   ├── models.py          # Cart, Order models
│   ├── views.py           # Cart & order views
│   ├── serializers.py     # Order serializers
│   └── urls.py            # Order endpoints
├── users/                  # Users app
│   ├── models.py          # Custom User model
│   ├── views.py           # Authentication views
│   └── serializers.py     # User serializers
├── db.sqlite3              # SQLite database (development)
├── requirements.txt        # Python dependencies
├── create_admin.py         # Admin creation script
├── create_test_data.py     # Test data generator
└── manage.py              # Django management script
📊 Database Schema
Key Models
User - Custom user model with email authentication

Category - Product categories (Electronics, Clothing, etc.)

Product - Store products with pricing and inventory

Cart - User shopping cart with items

Order - Customer orders with status tracking

ProductReview - User reviews and ratings

🧪 Testing
Default Test Credentials
Role	Username/Email	Password
Admin	admin / admin@marketflow.com	admin123
Customer	customer@marketflow.com	customer123
Running Tests
bash
python manage.py test products
python manage.py test orders
Using Postman/curl
bash
# Test public endpoints
curl http://127.0.0.1:8000/api/products/

# Test authenticated endpoints
curl -H "Authorization: Bearer YOUR_TOKEN" http://127.0.0.1:8000/api/cart/
🚀 Deployment
Deploy to Render (Recommended)
Push to GitHub

bash
git add .
git commit -m "Ready for deployment"
git push origin main
Create Render Account

Go to render.com

Sign up with GitHub

Create New Web Service

Connect your GitHub repository

Use these settings:

Build Command: pip install -r requirements.txt

Start Command: gunicorn core.wsgi:application

Environment Variables:

SECRET_KEY: Generate a secure key

DEBUG: False

DJANGO_SETTINGS_MODULE: core.settings

Deploy

Click "Create Web Service"

Your API will be live at https://your-app.onrender.com

Environment Variables
env
DEBUG=False
SECRET_KEY=your-secret-key-here
DJANGO_SETTINGS_MODULE=core.settings
📈 API Response Examples
Successful Product Response
json
{
  "id": 1,
  "name": "MacBook Pro 16\"",
  "description": "Apple MacBook Pro with M3 Pro chip",
  "price": "2499.99",
  "stock_quantity": 10,
  "category": {
    "id": 1,
    "name": "Electronics",
    "description": "Electronic devices and gadgets"
  },
  "average_rating": 4.5,
  "reviews": [...]
}
Cart Response
json
{
  "id": 1,
  "items": [
    {
      "id": 1,
      "product": {
        "id": 1,
        "name": "MacBook Pro 16\"",
        "price": "2499.99"
      },
      "quantity": 1,
      "total_price": "2499.99"
    }
  ],
  "total_price": "2499.99",
  "item_count": 1
}
🛡️ Security Features
JWT Authentication - Secure stateless authentication

SQL Injection Protection - Django ORM prevents SQL injection

Input Validation - All API inputs are validated

CORS Configuration - Controlled cross-origin requests

Rate Limiting Ready - Can be easily added with DRF

HTTPS Enforcement - In production environments

🤝 Contributing
Fork the repository

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit changes (git commit -m 'Add AmazingFeature')

Push to branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Django & Django REST Framework teams

ALX Software Engineering Program

Render for free hosting tier

Check the API Documentation

Open an issue in the GitHub repository

Contact the maintainer

MarketFlow - Powering modern e-commerce experiences with a robust, secure, and scalable API backend. 