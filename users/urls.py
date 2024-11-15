from django.urls import path
from .views import Signin, Signup
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('signin/', Signin.as_view(), name='token_obtain_pair'),
    path('signup/', Signup.as_view())
]