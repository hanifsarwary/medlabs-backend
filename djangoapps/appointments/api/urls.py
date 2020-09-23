from rest_framework.routers import DefaultRouter
from django.urls import path
from djangoapps.appointments.api.views import (
    AppointmentsViewSet, TimeSlotViewSet, TestsViewSet, AppointmentCreateAPIView, CategoriesAPIView)

router = DefaultRouter()
router.register(r'appointments', AppointmentsViewSet, basename='appointments')
router.register(r'time-slots', TimeSlotViewSet, basename='time_slots')
router.register(r'tests', TestsViewSet, basename='tests')
urlpatterns = [
    path('appointments/create/', AppointmentCreateAPIView.as_view()), 
    path('categories/', CategoriesAPIView.as_view()),
    ]
urlpatterns += router.urls
