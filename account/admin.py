from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class Admin(UserAdmin):
    list_display = ('email', 'phone', 'name', 'last_login', 'is_admin', 'is_agency',)
    search_fields = ('email', 'phone', 'name',)
    readonly_fields = ('date_joined', 'last_login',)
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = ((None,{'classes': ('wide',), 'fields':('email', 'phone', 'name', 'password1', 'password2', 'is_agency', 'is_admin', 'is_staff')}),)


admin.site.register(User, Admin)
