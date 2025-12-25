from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Add this
    updated_at = models.DateTimeField(auto_now=True)      # Add this
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')  # Add related_name
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField(default=0)
    image_url = models.URLField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='products')  # Add related_name
    created_at = models.DateTimeField(auto_now_add=True)  # ADD THIS LINE
    updated_at = models.DateTimeField(auto_now=True)      # ADD THIS LINE
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-created_at']  # Add default ordering

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Add this
    
    class Meta:
        unique_together = ['product', 'user']
    
    def __str__(self):
        return f"Review by {self.user} for {self.product}"