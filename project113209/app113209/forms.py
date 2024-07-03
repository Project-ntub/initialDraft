from django import forms
from .models import User, Role

#用戶名單，用於編輯用戶訊息
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone', 'department_id', 'position_id']

#角色表單，用於創建和編輯角色
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name', 'users']
