from django.contrib import admin
from lessons.models import Section


@admin.register(Section)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "trener", "section_name", "device_id")
    list_display_links = ("id", "trener", "section_name", "device_id")
