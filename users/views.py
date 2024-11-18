from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UsersSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import hashers
User = get_user_model()
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer
from utils.exceptions import handle_exceptions

class Signup(APIView):
    serializer_class = MyTokenObtainPairSerializer
    @handle_exceptions
    def post(self, request):
        new_user = UsersSerializer(data = request.data)
        new_user.is_valid(raise_exception=True)
        user = new_user.save()
        token_pair = RefreshToken.for_user(user)

        # generate token
        return Response({
            'user' : new_user.data,
            'token': str(token_pair.access_token)
        })
    




class Signin(APIView):
    serializer_class = MyTokenObtainPairSerializer
    @handle_exceptions
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = User.objects.get(email=email)

        if hashers.check_password(password, user.password):
            token_pair = RefreshToken.for_user(user)

            serialized_user = UsersSerializer(user)

            return Response({ 
                'user': serialized_user.data,
                'token': str(token_pair.access_token)
            })



        return Response({ 'detail': 'Unauthorized' }, status.HTTP_401_UNAUTHORIZED)
    



