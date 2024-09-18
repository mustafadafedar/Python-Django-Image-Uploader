from django.contrib import admin
from .models import upload


@admin.register(upload)
class uploadAdmin(admin.ModelAdmin):
    list_display = ('images','date')