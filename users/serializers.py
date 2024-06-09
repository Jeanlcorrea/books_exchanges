from rest_framework import serializers


class UserAddressSerializer(serializers.Serializer):
    cep = serializers.CharField(max_length=9)
    city = serializers.CharField(max_length=30)
    state = serializers.CharField(max_length=30)

class UserInputSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, help_text='username')
    password = serializers.CharField(max_length=200, help_text='password')
    email = serializers.CharField(max_length=254, help_text='user@email.com')
    address = UserAddressSerializer()


class UserOutputSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=254)
    is_active = serializers.BooleanField(default=True)
    is_staff = serializers.BooleanField(default=False)
    address = UserAddressSerializer()
