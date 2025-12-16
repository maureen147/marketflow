# MarketFlow - E-commerce API

.

## 🚀 Features

### ✅ **Week 1-2: Foundation & Products**
- **JWT Authentication** - Secure token-based authentication
- **Product Management** - Full CRUD operations for products
- **Category System** - Organized product categorization  
- **RESTful API** - Clean, structured API endpoints
- **Admin Permissions** - Role-based access control

### ✅ **Week 3-4: Advanced Features**
- **Product Search** - Search by name, description, or category
- **Advanced Filtering** - Filter by category, price range, stock status
- **Pagination** - Page-based navigation for product lists
- **Product Reviews** - Rating system with user reviews
- **Average Ratings** - Automatic rating calculation

## 📋 API Endpoints

### 🔐 Authentication
- `POST /api/token/` - Get JWT access token
- `POST /api/token/refresh/` - Refresh access token

### 📦 Products
- `GET /api/products/` - List all products (paginated)
- `POST /api/products/` - Create new product (Authenticated)
- `GET /api/products/{id}/` - Get product details
- `PUT /api/products/{id}/` - Update product (Authenticated)
- `DELETE /api/products/{id}/` - Delete product (Authenticated)

### 🔍 Search & Filtering
- `GET /api/products/search/?q=keyword` - Search products
- `GET /api/products/?category=1&min_price=50&max_price=500` - Filter products
- `GET /api/products/?in_stock=true` - Filter by stock availability

### 🏷️ Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create new category (Authenticated)

### ⭐ Reviews
- `GET /api/products/{id}/reviews/` - Get product reviews
- `POST /api/products/{id}/reviews/` - Add review (Authenticated)

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
```bash
# 1. Clone the repository
git clone https://github.com/maureen147/marketflow.git
cd marketflow

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run migrations
python manage.py migrate

# 6. Create superuser
python manage.py createsuperuser

# 7. Run development server
python manage.py runserver


marketflow/
├── core/              # Django project settings
├── products/          # Product management app
│   ├── models.py      # Product, Category, Review models
│   ├── serializers.py # API serializers
│   ├── views.py       # API views with search/filter
│   └── urls.py        # Product endpoints
├── users/             # User authentication app
├── .gitignore
├── requirements.txt   # Dependencies including django-filter
├── manage.py
└── README.md



🔧 Technologies Used
Django - Web framework

Django REST Framework - API framework

JWT Authentication - Secure token-based auth

SQLite - Database (Development)

django-filter - Advanced filtering

Python - Programming language

📖 Documentation
Admin Panel: http://localhost:8000/admin/

API Root: http://localhost:8000/api/

JWT Endpoints: /api/token/ and /api/token/refresh/

Product Search: /api/products/search/?q={query}

Product Reviews: /api/products/{id}/reviews/