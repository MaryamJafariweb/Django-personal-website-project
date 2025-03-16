from django.contrib import admin
from .models import Skills, Education

# Register your models here.
@admin.register(Skills)
class Skills(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(Education)
class Education(admin.ModelAdmin):
    list_display = ('title', 'description')
