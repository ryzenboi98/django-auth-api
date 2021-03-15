from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model,password_validation
from django.contrib.auth.hashers import make_password
from rest_framework.validators import UniqueValidator

User = get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    username = serializers.CharField(min_length=6, max_length=20, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(style={'input_type':'email'}, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(style={'input_type':'password'}, write_only=True)

    def validate_password(self, value):
        if value.isalnum() or not any(c.isdigit() for c in value) or value == value.lower():
            raise serializers.ValidationError('Password must contains one upper digit, one number and one symbol.')
        password_validation.validate_password(value, self.instance)
        return value

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        validated_data['first_name'] = validated_data['first_name'].capitalize()
        validated_data['last_name'] = validated_data['last_name'].capitalize()
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']