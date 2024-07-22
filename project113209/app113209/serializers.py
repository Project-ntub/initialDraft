from rest_framework import serializers
from .models import User, Module, Role, RolePermission

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone', 'is_verified', 'is_approved', 'department_id', 'position_id', 'branch_id', 'module', 'gender', 'is_staff', 'is_active', 'is_deleted', 'date_joined')

class ModuleSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ('id', 'name', 'user_count', 'is_deleted')

    def get_user_count(self, obj):
        return User.objects.filter(module=obj.name, is_active=True).count()

class RoleSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source='module.name', read_only=True)
    user_count = serializers.SerializerMethodField()
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Role
        fields = ('id', 'name', 'is_active', 'module', 'module_name', 'users', 'user_count', 'is_deleted')

    def get_user_count(self, obj):
        return obj.users.filter(is_active=True).count()

class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = ('id', 'role', 'permission_name', 'can_add', 'can_query', 'can_view', 'can_edit', 'can_delete', 'can_print', 'can_export', 'can_maintain', 'is_deleted')
