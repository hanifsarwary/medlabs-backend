from rest_framework import serializers

from djangoapps.appointments.models import Appointment, TimeSlot, Test
from djangoapps.users.api.v1.serializers import UserSerializer


class TimeSlotSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time_slot = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id

    def get_time_slot(self, obj):
        return obj.start_timestamp.strftime('%I:%M %p, %a %d-%m-%Y') + ' - ' + obj.end_timestamp.strftime('%I:%M %p, %a %d-%m-%Y')

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('__all__')


class AppointmentGetSerializer(serializers.ModelSerializer):
    """
    """
    user = UserSerializer()
    time_slot = TimeSlotSerializer()
    test = TestSerializer()
    class Meta:
        model = Appointment
        fields = ('id', 'appointment_date', 'time_slot', 'test', 'user', 'status')

class AppointmentPostSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Appointment
        fields = ('appointment_date', 'time_slot', 'test', 'user', 'status')
