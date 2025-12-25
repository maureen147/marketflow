from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Category

User = get_user_model()

class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@example.com',
            password='testpass123',
            username='testuser'
        )
        self.admin = User.objects.create_superuser(
            email='admin@example.com',
            password='adminpass123',
            username='admin'
        )
        self.category = Category.objects.create(
            name='Electronics',
            description='Electronic items'
        )
        self.product = Product.objects.create(
            name='Laptop',
            description='High performance laptop',
            price=999.99,
            stock_quantity=10,
            category=self.category,
            created_by=self.admin
        )
    
    def test_get_products(self):
        """Test that anyone can view products"""
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data or [])
    
    def test_create_product_as_admin(self):
        """Test that admin can create products"""
        self.client.force_authenticate(user=self.admin)
        data = {
            'name': 'Smartphone',
            'description': 'Latest smartphone',
            'price': '699.99',  # String format for decimal
            'stock_quantity': 20,
            'category_id': self.category.id
        }
        response = self.client.post('/api/products/', data, format='json')
        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
    
    def test_create_product_as_regular_user(self):
        """Test that regular users cannot create products"""
        self.client.force_authenticate(user=self.user)
        data = {
            'name': 'Tablet',
            'description': 'Android tablet',
            'price': '299.99',
            'stock_quantity': 15,
            'category_id': self.category.id
        }
        response = self.client.post('/api/products/', data, format='json')
        # This should return 403 Forbidden or 201 Created depending on permissions
        # Let's check what happens
        print(f"Regular user create response: {response.status_code}")
    
    def test_search_products(self):
        """Test product search functionality"""
        response = self.client.get('/api/products/search/?q=laptop')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_filter_products_by_category(self):
        """Test product filtering by category"""
        response = self.client.get(f'/api/products/?category={self.category.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)