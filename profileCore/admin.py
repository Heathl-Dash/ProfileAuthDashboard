from django.contrib import admin
from .models import DashboardProfile
from django.contrib.auth.admin import UserAdmin

admin.site.register(DashboardProfile.history.model)
@admin.register(DashboardProfile)
class DashboardProfileAdmin(UserAdmin):
    list_display = ('email', 'name', 'is_staff')
    search_fields = ('email', 'name')
    ordering = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('name', 'sex', 'weigth', 'heigth', 'emergency_phone_number', 'blood_type', 'points', 'age')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )