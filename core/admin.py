from django.contrib import admin

from core.models.user import (
    User
)

from django.contrib.admin.models import LogEntry

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phoneNumber', 'address')

@admin.register(LogEntry)
class LogEntryMonitor(admin.ModelAdmin):
    list_display = ('action_time','user','content_type','object_repr','change_message','action_flag')
    list_filter = ['action_time','user','content_type']
    ordering = ('-action_time',)

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False