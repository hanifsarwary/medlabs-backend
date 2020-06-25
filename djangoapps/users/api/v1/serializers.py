from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

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
        fields = ('id', 'username', 'email', 'address', 'phone', 'first_name', 'last_name', 'password', 'is_staff', 'password_confirmation')
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

