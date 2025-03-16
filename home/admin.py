from django.contrib import admin
from .models import PersonalInfo

# Register your models here.
@admin.register(PersonalInfo)
class PersonalIngoAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'description')
