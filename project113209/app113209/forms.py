from django import forms
from .models import User, Role, RolePermission

#用戶名單，用於編輯用戶訊息
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'department_id', 'position_id']

#角色表單，用於創建和編輯角色

class RoleForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'})
    )
    is_active = forms.BooleanField(required=False)
    module = forms.CharField(max_length=50)

    class Meta:
        model = Role
        fields = ['name', 'users', 'is_active', 'module']


class RolePermissionForm(forms.ModelForm):
    class Meta:
        model = RolePermission
        fields = ['permission_name', 'can_add', 'can_view', 'can_edit', 'can_delete', 'can_print', 'can_export', 'can_maintain']