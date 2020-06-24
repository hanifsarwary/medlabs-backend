from rest_framework.routers import DefaultRouter

from djangoapps.appointments.api.v1.views import AppointmentsViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentsViewSet, basename='appointments')

urlpatterns = router.urls
