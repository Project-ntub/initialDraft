from django import forms
from .models import User, Role, RolePermission, Module

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'department_id', 'position_id']

class RoleForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    is_active = forms.BooleanField(required=False)

    module = forms.ModelChoiceField(
        queryset=Module.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Role
        fields = ['name', 'users', 'is_active', 'module']

class RolePermissionForm(forms.ModelForm):
    class Meta:
        model = RolePermission
        fields = ['permission_name', 'can_add', 'can_query', 'can_view', 'can_edit', 'can_delete', 'can_print', 'can_export', 'can_maintain']
