from rest_framework import serializers

from djangoapps.appointments.models import Appointment, TimeSlot, Test, Panel, Category
from djangoapps.users.api.v1.serializers import UserSerializer


class TimeSlotSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    time_slot = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id

    def get_time_slot(self, obj):
        return obj.start_timestamp.strftime('%a, %m-%d-%Y, %I:%M %p') + ' - ' + obj.end_timestamp.strftime('%I:%M %p')


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class PanelSerializer(serializers.ModelSerializer):

    tests = TestSerializer(many=True)

    class Meta:
        model = Panel
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    panel = PanelSerializer(many=True, allow_null=True, source='panel_set')

    class Meta:
        model = Category
        fields = ('id', 'name', 'panel')


class AppointmentGetSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    time_slot = TimeSlotSerializer()
    panels = PanelSerializer(many=True)
    
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'
