# create_test_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model
from products.models import Category, Product, ProductReview
from orders.models import Cart

User = get_user_model()

print("=== CREATING TEST DATA ===")

# Create categories
print("1. Creating categories...")
electronics = Category.objects.create(
    name='Electronics',
    description='Electronic devices and gadgets'
)

clothing = Category.objects.create(
    name='Clothing', 
    description='Fashion and apparel'
)

books = Category.objects.create(
    name='Books',
    description='Books and literature'
)

# Get admin user
admin = User.objects.get(username='glowworm')

# Create regular customer
print("2. Creating customer user...")
customer = User.objects.create_user(
    email='customer@marketflow.com',
    password='customer123',
    username='customer'
)

# Create products
print("3. Creating products...")
products_data = [
    {
        'name': 'MacBook Pro 16"',
        'description': 'Apple MacBook Pro with M3 Pro chip',
        'price': 2499.99,
        'stock_quantity': 10,
        'category': electronics,
        'image_url': 'https://example.com/macbook.jpg'
    },
    {
        'name': 'Wireless Headphones',
        'description': 'Noise cancelling Bluetooth headphones',
        'price': 299.99,
        'stock_quantity': 50,
        'category': electronics,
        'image_url': 'https://example.com/headphones.jpg'
    },
    {
        'name': 'T-Shirt',
        'description': '100% Cotton premium t-shirt',
        'price': 29.99,
        'stock_quantity': 200,
        'category': clothing,
        'image_url': 'https://example.com/tshirt.jpg'
    },
    {
        'name': 'Jeans',
        'description': 'Slim fit denim jeans',
        'price': 89.99,
        'stock_quantity': 75,
        'category': clothing
    },
    {
        'name': 'Python Programming Book',
        'description': 'Learn Python programming from scratch',
        'price': 39.99,
        'stock_quantity': 100,
        'category': books
    },
    {
        'name': 'Smartphone',
        'description': 'Latest Android smartphone with 5G',
        'price': 799.99,
        'stock_quantity': 30,
        'category': electronics
    },
    {
        'name': 'Smart Watch',
        'description': 'Fitness tracking smart watch',
        'price': 199.99,
        'stock_quantity': 40,
        'category': electronics
    },
    {
        'name': 'Dress Shirt',
        'description': 'Formal dress shirt for office wear',
        'price': 59.99,
        'stock_quantity': 60,
        'category': clothing
    },
]

products = []
for data in products_data:
    product = Product.objects.create(
        **data,
        created_by=admin
    )
    products.append(product)
    print(f"   Created: {product.name} - ${product.price}")

# Add some reviews
print("4. Creating reviews...")
ProductReview.objects.create(
    product=products[0],
    user=customer,
    rating=5,
    comment='Excellent laptop! Fast and reliable.'
)

ProductReview.objects.create(
    product=products[1],
    user=customer,
    rating=4,
    comment='Great sound quality, battery could be better.'
)

ProductReview.objects.create(
    product=products[2],
    user=admin,
    rating=5,
    comment='Very comfortable and good quality fabric.'
)

print("\n=== SUMMARY ===")
print(f"Categories: {Category.objects.count()}")
print(f"Products: {Product.objects.count()}")
print(f"Users: {User.objects.count()}")
print(f"Reviews: {ProductReview.objects.count()}")
print("\n✅ Test data created successfully!")
print(f"\nAdmin login: glowworm / [your password]")
print(f"Customer login: customer@marketflow.com / customer123")
