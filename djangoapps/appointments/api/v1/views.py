from rest_framework.viewsets import ModelViewSet

from djangoapps.appointments.models import Appointment
from djangoapps.appointments.api.v1.serializers import AppointmentGetSerializer, AppointmentPostSerializer


class AppointmentsViewSet(ModelViewSet):
    """
    Viewset for "Appointment".
    """
    def get_queryset(self):
        """
        """
        return Appointment.objects.all()

    def get_serializer_class(self):
        """
        """
        if self.request.method == 'GET':
            return AppointmentGetSerializer

        return AppointmentPostSerializer
