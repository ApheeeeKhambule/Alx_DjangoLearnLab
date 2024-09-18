from rest_framework import serializers
from django.contrib.auth import get_user_model

# Getting the custom user model
CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # Explicitly declaring the password field as a write-only field
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        # Including fields for registration
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    # Overriding the create method to handle password hashing
    def create(self, validated_data):
        # Using the create_user method provided by Django for user creation
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],  # Password will be hashed automatically
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        return user
