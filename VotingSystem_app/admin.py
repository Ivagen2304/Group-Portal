from django.contrib import admin
from .models import Poll, Option, VoteRecord


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


class PollAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    inlines = [OptionInline]


admin.site.register(Poll, PollAdmin)
admin.site.register(VoteRecord)
