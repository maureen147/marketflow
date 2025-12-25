# users/serializers.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    # Accept 'email' field instead of 'username'
    username_field = 'email'
    
    def validate(self, attrs):
        # Map 'email' to 'username' for the parent class
        attrs['username'] = attrs.get('email', '')
        return super().validate(attrs)