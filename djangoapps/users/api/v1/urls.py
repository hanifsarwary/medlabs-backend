from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from djangoapps.users.api.v1.views import ActivateUserView, UsersViewSet

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')

urlpatterns = [
    url(r'^users/activate/', ActivateUserView, name='activate_view')
]
urlpatterns += router.urls
