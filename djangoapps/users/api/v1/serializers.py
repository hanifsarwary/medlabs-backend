from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from djangoapps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Basic user serializer.
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'address', 'phone', 'first_name', 'last_name', 'password', 'is_staff')
        extra_kwargs = ({ 'password': { 'write_only': True } })

    def validate(self, data):
        """
        Validate passwords are not empty.
        """
        validated_values = super(UserSerializer, self).validate(data)
        password = validated_values.get('password', '')

        if not password:
            raise serializers.ValidationError(
                {
                    'error': 'Passwords can not be empty'
                }
            )
        return validated_values

