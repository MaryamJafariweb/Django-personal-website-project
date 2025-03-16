from django.contrib import admin
from .models import Contact, ContactInfo

# Register your models here.
@admin.register(ContactInfo)
class ContactInfo(admin.ModelAdmin):
    list_display = ('email', 'phone_number', 'address')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', 'messages')
