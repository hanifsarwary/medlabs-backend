from rest_framework.routers import DefaultRouter

from djangoapps.appointments.api.views import AppointmentsViewSet, TimeSlotViewSet, TestsViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentsViewSet, basename='appointments')
router.register(r'time-slots', TimeSlotViewSet, basename='time_slots')
router.register(r'tests', TestsViewSet, basename='tests')

urlpatterns = router.urls
