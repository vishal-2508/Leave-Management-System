from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# Create your views here.

def login_page(request):
    return render(request, 'accounts/login.html')

def registration_page(request):
    return render(request, 'accounts/registration.html')


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        ## serializer contain corrent user data 
        serializer = self.get_serializer(data=request.data)
        # Check if the data is valid before proceeding
        if serializer.is_valid():
            print('Serializer data (valid):', serializer.validated_data)
        else:
            print('Serializer errors:', serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # Call the original post method logic to generate tokens
        # The parent's post method will return the Response object with tokens
        response = super().post(request, *args, **kwargs) 
        user = serializer.user
        final_response = response.data
        final_response["user_type"] = user.user_type
        final_response["user"] = user.id
        return Response(final_response)


class RegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer_class = UserSerializers()
            serializer_class.create_user(request.data)
            return Response({
              "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


