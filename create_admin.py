# create_admin.py
import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

try:
    # Check if admin already exists
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@marketflow.com',
            password='admin123'
        )
        print("✅ Admin user created: admin / admin123")
    else:
        print("ℹ️ Admin user already exists")
except Exception as e:
    print(f"❌ Error creating admin: {e}")
    sys.exit(1)