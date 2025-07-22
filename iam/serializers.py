from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, trim_whitespace=True, allow_blank=False, max_length=50)
    password = serializers.CharField(required=True, write_only=True, allow_blank=False)

