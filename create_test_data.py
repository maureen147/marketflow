# create_test_data.py
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from products.models import Category, Product, ProductReview
from orders.models import Cart

User = get_user_model()

print("=== CREATING TEST DATA ===")

# CREATE ADMIN USER FIRST (FIXED)
print("1. Creating admin user...")
try:
    admin, created = User.objects.get_or_create(
        username='admin',  # Changed from 'glowworm' to 'admin'
        defaults={
            'email': 'admin@marketflow.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        admin.set_password('admin123')  # Set password for new admin
        admin.save()
        print("   Created new admin: admin / admin123")
    else:
        print("   Admin user already exists")
except Exception as e:
    print(f"   Error creating admin: {e}")
    sys.exit(1)

# CREATE CUSTOMER USER
print("2. Creating customer user...")
try:
    customer, created = User.objects.get_or_create(
        username='customer',
        defaults={
            'email': 'customer@marketflow.com',
        }
    )
    if created:
        customer.set_password('customer123')
        customer.save()
        print("   Created customer: customer@marketflow.com / customer123")
    else:
        print("   Customer already exists")
except Exception as e:
    print(f"   Error creating customer: {e}")

# CREATE CATEGORIES
print("3. Creating categories...")
categories_data = [
    {'name': 'Electronics', 'description': 'Electronic devices and gadgets'},
    {'name': 'Clothing', 'description': 'Fashion and apparel'},
    {'name': 'Books', 'description': 'Books and literature'},
]

categories = {}
for cat_data in categories_data:
    category, created = Category.objects.get_or_create(
        name=cat_data['name'],
        defaults={'description': cat_data['description']}
    )
    categories[cat_data['name'].lower()] = category
    print(f"   Category: {category.name}")

# CREATE PRODUCTS
print("4. Creating products...")
products_data = [
    {
        'name': 'MacBook Pro 16"',
        'description': 'Apple MacBook Pro with M3 Pro chip',
        'price': 2499.99,
        'stock_quantity': 10,
        'category': categories['electronics'],
        'image_url': 'https://example.com/macbook.jpg'
    },
    {
        'name': 'Wireless Headphones',
        'description': 'Noise cancelling Bluetooth headphones',
        'price': 299.99,
        'stock_quantity': 50,
        'category': categories['electronics'],
        'image_url': 'https://example.com/headphones.jpg'
    },
    {
        'name': 'T-Shirt',
        'description': '100% Cotton premium t-shirt',
        'price': 29.99,
        'stock_quantity': 200,
        'category': categories['clothing'],
        'image_url': 'https://example.com/tshirt.jpg'
    },
    {
        'name': 'Jeans',
        'description': 'Slim fit denim jeans',
        'price': 89.99,
        'stock_quantity': 75,
        'category': categories['clothing']
    },
    {
        'name': 'Python Programming Book',
        'description': 'Learn Python programming from scratch',
        'price': 39.99,
        'stock_quantity': 100,
        'category': categories['books']
    },
]

products = []
for data in products_data:
    product, created = Product.objects.get_or_create(
        name=data['name'],
        defaults={
            'description': data['description'],
            'price': data['price'],
            'stock_quantity': data['stock_quantity'],
            'category': data['category'],
            'created_by': admin,
            'image_url': data.get('image_url')
        }
    )
    products.append(product)
    print(f"   Product: {product.name} - ${product.price}")

# CREATE REVIEWS (only if customer exists)
print("5. Creating reviews...")
try:
    if products and customer:
        ProductReview.objects.get_or_create(
            product=products[0],
            user=customer,
            defaults={
                'rating': 5,
                'comment': 'Excellent laptop! Fast and reliable.'
            }
        )
        ProductReview.objects.get_or_create(
            product=products[1],
            user=customer,
            defaults={
                'rating': 4,
                'comment': 'Great sound quality, battery could be better.'
            }
        )
        print("   Created 2 reviews")
except Exception as e:
    print(f"   Error creating reviews: {e}")

print("\n=== SUMMARY ===")
print(f"Categories: {Category.objects.count()}")
print(f"Products: {Product.objects.count()}")
print(f"Users: {User.objects.count()}")
try:
    print(f"Reviews: {ProductReview.objects.count()}")
except:
    print("Reviews: N/A")

print("\n✅ Test data created successfully!")
print(f"\nAdmin login: admin / admin123")
print(f"Customer login: customer@marketflow.com / customer123")