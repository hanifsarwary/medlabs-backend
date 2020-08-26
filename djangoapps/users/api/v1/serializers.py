from django_rest_passwordreset.serializers import PasswordTokenSerializer as default_serializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.utils.translation import ugettext_lazy as _
from djangoapps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    Basic user serializer.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'address', 'phone', 'first_name', 'last_name', 'is_staff')


class UserSignUpSerializer(serializers.ModelSerializer):
    """
    Basic user serializer.
    """
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'address', 'phone', 'first_name', 'last_name', 'password', 'password_confirmation')
        extra_kwargs = ({ 'password': { 'write_only': True } })

    def validate(self, data):
        """
        Validate passwords are not empty.
        """
        validated_values = super(UserSignUpSerializer, self).validate(data)
        password = validated_values.get('password', '')
        password_confirmation = validated_values.pop('password_confirmation')

        if not password or not password_confirmation:
            raise serializers.ValidationError(
                {
                    'error': 'Passwords can not be empty'
                }
            )

        if password != password_confirmation:
            raise serializers.ValidationError(
                {
                    'error': 'Passwords do not match'
                }
            )

        return validated_values


class PasswordTokenSerializer(default_serializer):
    """
    Password token serializer override.
    """
    password1 = serializers.CharField(label=_("Password Confirmation"), style={'input_type': 'password'})

    def validate(self, data):
        """
        Validate passwords are same.
        """
        password = data.get('password')
        password1 = data.get('password1')
        if not password or not password1:
            raise serializers.ValidationError(
                {
                    'error': 'Passwords can not be empty'
                }
            )

        if password != password1:
            raise serializers.ValidationError(
                {
                    'error': 'Passwords do not match'
                }
            )

        return super(PasswordTokenSerializer, self).validate(data)


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        """
        Override validate method to add user to return data.
        """
        data = super().validate(attrs)
        user = User.objects.get(username=attrs.get('username'))
        data['user'] = UserSerializer(user).data
        return data
