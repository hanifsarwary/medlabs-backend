from django.contrib import admin

from djangoapps.appointments.models import Appointment

class AppointmentsAdmin(admin.ModelAdmin):
    """
    Admin interface for the "Appointment" object.
    """
    search_fields = ['title']
    list_display = ['title', 'appointment_date', 'start_time', 'end_time', 'customer', 'status']
    list_filter = ['status', 'appointment_date']
    list_per_page = 25
    ordering = ['-id']

    def customer(self, obj):
        return obj.user.username

admin.site.register(Appointment, AppointmentsAdmin)
