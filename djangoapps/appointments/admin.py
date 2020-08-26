from django.contrib import admin

from djangoapps.appointments.models import Appointment, Test

class AppointmentsAdmin(admin.ModelAdmin):
    """
    Admin interface for the "Appointment" object.
    """
    search_fields = ['test_title']
    list_display = ['test', 'appointment_date', 'time_slot', 'customer', 'status']
    list_filter = ['status', 'appointment_date']
    list_per_page = 25
    ordering = ['-id']

    def customer(self, obj):
        return obj.user.username

admin.site.register(Appointment, AppointmentsAdmin)
admin.site.register(Test)
