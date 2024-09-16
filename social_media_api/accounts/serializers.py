from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.authtoken.models import Token

# Get the custom user model
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Using CharField for passwords to enforce write-only access
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'bio', 'profile_picture']

    # Validating that both password fields match
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    # Custom method for creating a new user
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        user.set_password(validated_data['password'])  # Set hashed password
        user.save()

        # Create a token for the new user
        Token.objects.create(user=user)

        return user
