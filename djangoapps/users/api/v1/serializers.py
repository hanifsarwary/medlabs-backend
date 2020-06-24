from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from djangoapps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Basic user serializer.
    """
    password_confirmation = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'address', 'phone', 'first_name', 'last_name', 'password', 'password_confirmation', 'is_staff')
        extra_kwargs = ({ 'password': { 'write_only': True } })

    def validate(self, data):
        """
        Validate passwords are same.
        """
        validated_values = super(UserSerializer, self).validate(data)
        password = validated_values.get('password', '')
        password_confirmation = validated_values.get('password_confirmation', '')
        if password != password_confirmation:
            raise serializers.ValidationError(
                {
                    'error': 'The given passwords don\'t match'
                }
            )

        validated_values.pop('password_confirmation')
        return validated_values

