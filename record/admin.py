from django.contrib import admin
from .models import Rescue,Attachment

# Register your models here.

@admin.register(Rescue)
class RescueAdmin(admin.ModelAdmin):
    pass

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    pass