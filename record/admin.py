from django.contrib import admin
from .models import RescueInfo

# Register your models here.

@admin.register(RescueInfo)
class RescueInfoAdmin(admin.ModelAdmin):
    pass