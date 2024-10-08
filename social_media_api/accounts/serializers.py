
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

# Import the CustomUser model using get_user_model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'bio', 'profile_picture']

    def create(self, validated_data):
        # Use create_user to handle password hashing
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        
        # Create an authentication token for the user
        Token.objects.create(user=user)
        return user

  ["serializers.CharField()", "get_user_model().objects.create_user"]
