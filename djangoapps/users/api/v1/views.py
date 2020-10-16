from django_rest_passwordreset.views import ResetPasswordConfirm as default_password_reset
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from djangoapps.users.models import User, DisplayUserReviews, CareerVacancy, JobApplication
from djangoapps.users.api.v1.serializers import (
    PasswordTokenSerializer, DisplayUserReviewsSerializer,
    UserSerializer, CareerVacancySerializer, JobApplicationSerializer,
    UserSignUpSerializer,
    UserTokenObtainPairSerializer, 
)
from constance import config

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
            permission_classes = [AllowAny]

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


class UserTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserTokenObtainPairSerializer


class ResetPasswordConfirm(default_password_reset):
    serializer_class = PasswordTokenSerializer


class DisplayUserReviewsViewSet(ModelViewSet):

    serializer_class = DisplayUserReviewsSerializer
    queryset = DisplayUserReviews.objects.all()
    permission_classes = [AllowAny]


class CareerVacancyViewSet(ModelViewSet):

    serializer_class = CareerVacancySerializer
    queryset = CareerVacancy.objects.all()
    permission_classes = [AllowAny]


class JobApplicationViewSet(ModelViewSet):

    serializer_class = JobApplicationSerializer
    queryset = JobApplication.objects.all()
    permission_classes = [AllowAny]


class WhoWeAreTextAPIView(APIView):

    permission_classes = [AllowAny]
    def get(self, request):
        return Response({'text': config.WHO_WE_ARE})