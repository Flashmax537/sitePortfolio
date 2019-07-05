from django.contrib import admin
from apps.main.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass