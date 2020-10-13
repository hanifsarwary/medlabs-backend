from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.db.models import Count, Q
from datetime import datetime
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from djangoapps.appointments.models import Appointment, TimeSlot, Test, Category
from djangoapps.appointments.api.serializers import (
    AppointmentGetSerializer, AppointmentPostSerializer, TimeSlotSerializer, TestSerializer, CategorySerializer,
    UpdateAppointmentStatusSerializer)
from djangoapps.users.tasks import send_email
import json

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
            time_slot = TimeSlot.objects.get(pk=request.data.get('time_slot'))
            time_slot.appointment_count += 1
            time_slot.save()
            recipient_list = []
            message = "An new Appointment has been created by user: {}. \n Alloted TimeSlot: {}".format(
                request.user.username, str(time_slot))
            if request.user.email:
                recipient_list.append(request.user.email)
            recipient_list.append("hanifsarwari.nuces@gmail.com")
            recipient_list.append('appointments@medscreenlabs.com')
            send_email.delay(recipient_list, "Appointment created", message)
             
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response({}, status=status.HTTP_400_BAD_REQUEST)



class UpdateAppointmentStatusAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = UpdateAppointmentStatusSerializer
    
    def get_queryset(self):

        return Appointment.objects.filter(pk=self.kwargs.get('pk'))
    
    def paid_mail_to_user(self, request):
        appointment_obj = Appointment.objects.get(pk=self.kwargs.get('pk'))

        if request.data.get('status') == 'paid':
            message = "User {} has paid {} USD for his appointment at {}".format(
                self.request.user.username, str(appointment_obj.total_price), str(appointment_obj.time_slot))
            subject = "Payment confirmation"
            recipient_list = []
            if request.user.email:
                recipient_list.append(request.user.email)
            recipient_list.append("hanifsarwari.nuces@gmail.com")
            recipient_list.append('appointments@medscreenlabs.com')
            send_email.delay(recipient_list, subject, message)

    def put(self, request, *args, **kwargs):
        update_response = self.update(request, *args, **kwargs)
        self.paid_mail_to_user(request)
        return update_response

    def patch(self, request, *args, **kwargs):
        update_response = self.partial_update(request, *args, **kwargs)
        self.paid_mail_to_user(request)
        return update_response
    

class TimeSlotViewSet(ModelViewSet):
    """
    Viewset for "TimeSlot".
    """
    serializer_class = TimeSlotSerializer
    allowed_methods = ('get')

    def get_queryset(self):
        """
        """
        queryset = TimeSlot.objects.all()
        date = self.request.query_params.get('date')
        if date:
            date = datetime.strptime(date, '%Y-%m-%d')
            queryset = queryset.filter(start_timestamp__date=date, appointment_count__lt=4)

        return queryset


class TestsViewSet(ModelViewSet):
    """
    Viewset for "Test".
    """
    serializer_class = TestSerializer
    allowed_methods = ('get')
    queryset = Test.objects.all()


class CategoriesAPIView(ListAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent_category__isnull=True)