from django.contrib import admin
from django.contrib.auth.models import Group
from django.urls import reverse
from django.utils.html import format_html

from djangoapps.users.models import User, DisplayUserReviews, CareerVacancy, JobApplication


class UsersAdmin(admin.ModelAdmin):
    """
    Admin interface for the "User" object.
    """
    def link_to_actions(self, obj):
        edit_link = reverse("admin:users_user_change", args=[obj.id])
        delete_link = reverse("admin:users_user_delete", args=[obj.id])
        return format_html('<a href="{}">{}</a> <hr style="width: 3px; height: 10px; display: inline-block;"> <a '
                               'href="{}">{}</a>', edit_link, 'Edit', delete_link, 'Delete')
    link_to_actions.short_description = 'Actions'

    fields = ['username', 'email', 'first_name', 'last_name', 'address', 'phone', 'is_staff', 'is_active']
    list_display = ['username', 'email', 'full_name', 'address', 'phone', 'link_to_actions']
    list_filter = ['is_staff', 'is_active']
    list_per_page = 25
    ordering = ['-id']
    search_fields = ['username', 'email']

admin.site.register(User, UsersAdmin)
admin.site.unregister(Group)
admin.site.register(JobApplication)
admin.site.register(CareerVacancy)
admin.site.register*=(DisplayUserReviews)