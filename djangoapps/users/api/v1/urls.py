from rest_framework.routers import DefaultRouter

from django.conf.urls import url

from djangoapps.users.api.v1.views import (
    ActivateUserView, UsersViewSet, DisplayUserReviewsViewSet, CareerVacancyViewSet, JobApplicationViewSet,
    WhoWeAreTextAPIView)

router = DefaultRouter()
router.register(r'users', UsersViewSet, basename='users')
router.register(r'user-reviews', DisplayUserReviewsViewSet, basename='user-reviews')
router.register(r'careers', CareerVacancyViewSet, basename='careers')
router.register(r'job-applications', JobApplicationViewSet, basename='job-application')


urlpatterns = [
    url(r'^users/activate/', ActivateUserView, name='activate_view'),
    url(r'^who-we-are/', WhoWeAreTextAPIView.as_view, name='who_we_are_view')
]
urlpatterns += router.urls
