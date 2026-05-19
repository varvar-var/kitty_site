from django.contrib import admin
from . models import Volunteer, Cat

# Register your models here.
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email')
    empty_value_display = '<<Empty>>'

@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'age', 'description')
    search_fields = ('name',)
    empty_value_display = '<<Empty>>'