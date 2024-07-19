# app113209/serializers.py
from rest_framework import serializers
from .models import User, Module, Role, RolePermission

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone', 'is_verified', 'is_approved', 'department_id', 'position_id', 'branch_id', 'module', 'gender', 'is_staff', 'is_active', 'is_deleted', 'date_joined')

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('id', 'name', 'is_deleted')

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name', 'is_active', 'module', 'is_deleted')

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = ('id', 'role', 'permission_name', 'can_add', 'can_query', 'can_view', 'can_edit', 'can_delete', 'can_print', 'can_export', 'can_maintain', 'is_deleted')
