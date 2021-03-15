from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model,password_validation
from django.contrib.auth.hashers import make_password

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(min_length=6, max_length=20)
    email = serializers.EmailField(style={'input_type':'email'})
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    # h

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']