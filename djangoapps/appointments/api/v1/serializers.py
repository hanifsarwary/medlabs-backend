from rest_framework import serializers

from djangoapps.appointments.models import Appointment
from djangoapps.users.api.v1.serializers import UserSerializer


class AppointmentGetSerializer(serializers.ModelSerializer):
    """
    """
    user = UserSerializer()
    class Meta:
        model = Appointment
        fields = ('id', 'title', 'description', 'appointment_date', 'start_time', 'end_time', 'user', 'status')

class AppointmentPostSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Appointment
        fields = ('title', 'description', 'appointment_date', 'start_time', 'end_time', 'user', 'status')
