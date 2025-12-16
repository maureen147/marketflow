from django.urls import path
from .views import (
    ProductListView, ProductDetailView, CategoryListView,
    ProductSearchView, ProductReviewListView
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
    path('products/<int:product_id>/reviews/', ProductReviewListView.as_view(), name='product-reviews'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
