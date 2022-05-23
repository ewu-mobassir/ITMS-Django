from django.contrib import admin
from districts.models import District


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_name',)
    search_fields = ('district_name',)
    ordering = ('district_name',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
# Register your models here.
