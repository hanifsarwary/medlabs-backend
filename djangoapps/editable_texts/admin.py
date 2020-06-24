from django.contrib import admin

from djangoapps.editable_texts.models import EditableText

class EditableTextAdmin(admin.ModelAdmin):
    """
    Admin interface for the "Appointment" object.
    """
    search_fields = ['key']
    list_display = ['key', 'value']
    list_per_page = 25
    ordering = ['-id']

admin.site.register(EditableText, EditableTextAdmin)
