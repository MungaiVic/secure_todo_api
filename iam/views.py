from rest_framework.response import Response
from rest_framework.decorators import api_view

from iam.serializers import LoginSerializer


@api_view(['POST', 'GET'])
def login(request):
    login_serializer = LoginSerializer(data=request.data)
    login_serializer.is_valid(raise_exception=True)
    return Response({"message": "Hello there"})
