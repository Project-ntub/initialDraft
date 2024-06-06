from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'department_id', 'position_id', 'branch_id', 'module', 'gender', 'is_approved')
    list_filter = ('department_id', 'position_id', 'branch_id', 'gender', 'is_approved')

admin.site.register(User, UserAdmin)
