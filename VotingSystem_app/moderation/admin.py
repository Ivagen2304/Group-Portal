from django.contrib import admin
from .models import Poll, PollOption, Notification
class OptionInline(admin.TabularInline):
    model = PollOption
    extra = 0
@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [OptionInline]
    list_display = ('question','creator','send_at','sent','created_at')
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user','poll','created_at','read')
