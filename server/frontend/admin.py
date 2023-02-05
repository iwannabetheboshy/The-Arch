from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email_address', 'city', 'phone')
