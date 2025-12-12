# MarketFlow - E-commerce API

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django%20REST%20Framework-092E20?style=for-the-badge&logo=django&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![ALX](https://img.shields.io/badge/ALX-Capstone_Project-blue)

A Django REST Framework-based e-commerce backend API for ALX Software Engineering capstone project.

## ��� Features

- ✅ **JWT Authentication** - Secure token-based authentication
- ✅ **Product Management** - Full CRUD operations for products
- ✅ **Category System** - Organized product categorization  
- ✅ **RESTful API** - Clean, structured API endpoints
- ✅ **SQLite Database** - Easy setup and development

## ��� API Endpoints

### Authentication
- `POST /api/token/` - Get JWT access token
- `POST /api/token/refresh/` - Refresh access token

### Products
- `GET /api/products/` - List all products
- `POST /api/products/` - Create new product (Authenticated)
- `GET /api/products/{id}/` - Get product details
- `PUT /api/products/{id}/` - Update product (Authenticated)
- `DELETE /api/products/{id}/` - Delete product (Authenticated)

### Categories
- `GET /api/categories/` - List all categories
- `POST /api/categories/` - Create new category (Authenticated)

## ���️ Installation

### Prerequisites
- Python 3.8+
- pip

### Setup
\`\`\`bash
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
\`\`\`

## ��� Testing the API

### Get JWT Token
\`\`\`bash
curl -X POST http://localhost:8000/api/token/ \
     -H "Content-Type: application/json" \
     -d '{"username": "admin", "password": "your_password"}'
\`\`\`

### List Products
\`\`\`bash
curl http://localhost:8000/api/products/
\`\`\`

### Create Product
\`\`\`bash
curl -X POST http://localhost:8000/api/products/ \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -d '{
       "name": "Test Product",
       "description": "Product description",
       "price": 99.99,
       "stock_quantity": 10,
       "category_id": 1
     }'
\`\`\`

## ��� Project Structure

\`\`\`
marketflow/
├── core/              # Django project settings
├── products/          # Product management app
├── users/            # User authentication app
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
\`\`\`

## ��� Technologies Used

- **Django** - Web framework
- **Django REST Framework** - API framework  
- **JWT** - Authentication
- **SQLite** - Database
- **Python** - Programming language

## ��� Documentation

- **Admin Panel**: http://localhost:8000/admin/
- **API Root**: http://localhost:8000/api/
- **JWT Endpoints**: \`/api/token/\` and \`/api/token/refresh/\`

## ��� Author

**Maureen** - ALX Software Engineering Student

- GitHub: [@maureen147](https://github.com/maureen147)


