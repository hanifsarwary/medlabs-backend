from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from djangoapps.users.models import User
from djangoapps.users.api.v1.serializers import UserSerializer, UserSignUpSerializer

class UsersViewSet(ModelViewSet):
    """
    Viewset for "User".
    """
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Get permission class according to viewset action.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        """
        """
        if self.action == 'create':
            return UserSignUpSerializer

        return UserSerializer

@api_view(['GET'])
@permission_classes([AllowAny])
def ActivateUserView(request):
    """
    View to activate email.
    """
    token = request.GET.get('token')
    try:
        token = AccessToken(token)
        user_id = token.get('user_id', None)
        user = User.objects.get(id=user_id)
        if user.is_active == True:
            return Response('User is already activated', status=status.HTTP_400_BAD_REQUEST)

        user.is_active = True
        user.save()
        return Response(data='User activated', status=status.HTTP_200_OK)
    except Exception as error:
        return Response(error, status=status.HTTP_400_BAD_REQUEST)


class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        """
        Override validate method to add user to return data.
        """
        data = super().validate(attrs)
        user = User.objects.get(username=attrs.get('username'))
        data['user'] = UserSerializer(user).data
        return data


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer
