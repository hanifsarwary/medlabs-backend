from django.contrib import admin

from djangoapps.media.models import EditableText, Media

class EditableTextAdmin(admin.ModelAdmin):
    """
    Admin interface for the "Appointment" object.
    """
    search_fields = ['key']
    list_display = ['key', 'value']
    list_per_page = 25
    ordering = ['-id']

admin.site.register(EditableText, EditableTextAdmin)
admin.site.register(Media)
