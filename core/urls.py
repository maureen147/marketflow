from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import EmailTokenObtainPairView  # Import custom view

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>MarketFlow API</title>
        <style>
            body { font-family: Arial; margin: 40px; }
            h1 { color: #333; }
            ul { line-height: 1.8; }
            a { color: #0066cc; text-decoration: none; }
            a:hover { text-decoration: underline; }
            .container { max-width: 800px; margin: 0 auto; }
            .endpoint { background: #f5f5f5; padding: 10px; margin: 10px 0; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>MarketFlow E-commerce API</h1>
            <p>Your ALX Capstone Project is running successfully!</p>
            
            <h2>Available Endpoints:</h2>
            <div class="endpoint">
                <strong>GET</strong> <a href="/api/products/">/api/products/</a> - List all products
            </div>
            <div class="endpoint">
                <strong>GET</strong> <a href="/api/categories/">/api/categories/</a> - Product categories
            </div>
            <div class="endpoint">
                <strong>POST</strong> /api/register/ - Register new user (email, username, password)
            </div>
            <div class="endpoint">
                <strong>POST</strong> /api/token/ - Get JWT Token (email, password)
            </div>
            <div class="endpoint">
                <strong>POST</strong> /api/token/refresh/ - Refresh JWT Token
            </div>
            <div class="endpoint">
                <strong>GET/POST</strong> /api/cart/ - Cart management (requires authentication)
            </div>
            
            <h2>Quick Links:</h2>
            <ul>
                <li><a href="/admin/">Admin Panel</a> - Manage products & orders</li>
                <li><a href="/api/products/search/?q=laptop">Search Products</a> - Try search functionality</li>
            </ul>
            
            <h2>Test Credentials:</h2>
            <ul>
                <li><strong>Admin:</strong> admin@marketflow.com / admin123</li>
                <li><strong>Customer:</strong> customer@marketflow.com / customer123</li>
            </ul>
            
            <p><strong>For Postman/API Testing:</strong> Use Bearer token authentication after login.</p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    
    # Authentication endpoints
    path('api/register/', include('users.urls')),  # Includes registration
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # App URLs
    path('api/', include('products.urls')),
    path('api/', include('orders.urls')),
]