from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from iam.serializers import LoginSerializer


@api_view(['POST'])
def login(request):
    login_serializer = LoginSerializer(data=request.data)
    login_serializer.is_valid(raise_exception=True)
    # Validate credentials
    validated_data = login_serializer.validated_data
    username = validated_data['username']
    password = validated_data['password']

    valid_user = User.objects.filter(username=username).first()
    if valid_user:
        validated_user = authenticate(request, username=username, password=password)
        if validated_user:
            # We will add more authentication and authorization condiments later
            return Response({"message": "Login successful"})

    return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

