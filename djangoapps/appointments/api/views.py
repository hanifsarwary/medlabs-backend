from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Count, Q
from datetime import datetime
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView
from djangoapps.appointments.models import Appointment, TimeSlot, Test, Category
from djangoapps.appointments.api.serializers import (
    AppointmentGetSerializer, AppointmentPostSerializer, TimeSlotSerializer, TestSerializer, CategorySerializer,
    UpdateAppointmentStatusSerializer)
from users.tasks import send_email


class AppointmentsViewSet(ModelViewSet):
    """
    Viewset for "Appointment".
    """
    def get_queryset(self):
        """
        """
        username = self.request.query_params.get('user')
        active = True if self.request.query_params.get('active') == 'true' else False
        queryset = Appointment.objects.all()
        if username:
            queryset = queryset.filter(user__username=username)
        if active:
            queryset = queryset.filter(status='pending')
        else:
            queryset = queryset.filter(~Q(status='pending'))

        return queryset
    

    def get_serializer_class(self):
        """
        """
        if self.request.method == 'GET':
            return AppointmentGetSerializer

        return AppointmentPostSerializer


class AppointmentCreateAPIView(CreateAPIView):

    serializer_class = AppointmentPostSerializer
    queryset = Appointment.objects.all()

    def create(self, request, *args, **kwargs):
        pending_appointment = Appointment.objects.filter(user=request.user, status=Appointment.STATUS.pending)
        if not pending_appointment:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            recipient_list = []
            message = "An new Appointment has been created by user: {}".format(request.user.username)
            if request.user.email:
                recipient_list.append(request.user.email)
            recipient_list.append("hanifsarwari.nuces@gmail.com")
            send_email.delay(recipient_list, "Appointment created", message)
             
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response({}, status=status.HTTP_400_BAD_REQUEST)



class UpdateAppointmentStatusAPIView(RetrieveUpdateAPIView):

    serializer_class = UpdateAppointmentStatusSerializer
    
    def get_queryset(self):

        return Appointment.objects.filter(pk=self.kwargs.get('pk'))


class TimeSlotViewSet(ModelViewSet):
    """
    Viewset for "TimeSlot".
    """
    serializer_class = TimeSlotSerializer
    allowed_methods = ('get')

    def get_queryset(self):
        """
        """
        date = self.request.query_params.get('date')
        if date:
            date = datetime.strptime(date, '%Y-%m-%d')
            return TimeSlot.objects.annotate(appointment_count=Count('appointment')).filter(start_timestamp__date=date, appointment_count__lte=5)

        return TimeSlot.objects.all()


class TestsViewSet(ModelViewSet):
    """
    Viewset for "Test".
    """
    serializer_class = TestSerializer
    allowed_methods = ('get')
    queryset = Test.objects.all()


class CategoriesAPIView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()