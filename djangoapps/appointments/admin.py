from django.contrib import admin

from djangoapps.appointments.models import Appointment, Test, Panel

class AppointmentsAdmin(admin.ModelAdmin):
    """
    Admin interface for the "Appointment" object.
    """
    search_fields = ['test_title']
    list_display = ['appointment_date', 'time_slot', 'user', 'status']
    list_filter = ['status', 'appointment_date']
    raw_id_fields = ['time_slot']
    list_per_page = 25
    ordering = ['-id']

    def customer(self, obj):
        return obj.user.username


class TestsInline(admin.StackedInline):
    model = Panel.tests.through

class PanelAdmin(admin.ModelAdmin):
    inlines = [
        TestsInline,
    ]
    exclude = ('tests',)



admin.site.register(Appointment, AppointmentsAdmin)
admin.site.register(Test)
admin.site.register(Panel, PanelAdmin)

