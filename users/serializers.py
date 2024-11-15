from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation, hashers
from django.core.validators import validate_email
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        password = data.get("password")
        confirm_password = data.get("confirm_password") 
        email = data.get("email")


        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        
        # Validate the password and email
        password_validation.validate_password(password=password)
        validate_email(email)

        data["password"] = hashers.make_password(password)  # Hash the password

        data.pop("confirm_password") 
         

        return data 


    class Meta:
        model = User
        fields = ["id", "email", "username", "password", "confirm_password", "first_name", "last_name", "role"]





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['role'] = user.role

        return token