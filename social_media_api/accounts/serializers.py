from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  # For creating tokens

# Getting the custom user model
CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Explicitly declare the password field as a write-only field
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        # Include fields for registration
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    # Override the create method to handle password and token creation
    def create(self, validated_data):
        # Create the user using Django's create_user method, which handles password hashing
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        
        # Create the token for the new user
        Token.objects.create(user=user)
        
        return user
