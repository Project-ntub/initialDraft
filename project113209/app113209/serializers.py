from rest_framework import serializers
from .models import User, Module, Role, RolePermission

class ModuleSerializer(serializers.ModelSerializer):
    user_count = serializers.SerializerMethodField()

    class Meta:
        model = Module
        fields = ('id', 'name', 'user_count', 'is_deleted')
        extra_kwargs = {
            'name': {'required': True},
        }

    def get_user_count(self, obj):
        return User.objects.filter(roles__module=obj, is_active=True).count()

class UserSerializer(serializers.ModelSerializer):
    role = serializers.StringRelatedField()  # 將 read_only=True 設為避免與巢狀序列化器衝突
    module = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'module', 'phone', 'is_verified', 'is_approved', 'department_id', 'position_id', 'branch_id', 'module', 'gender', 'is_staff', 'is_active', 'is_deleted', 'date_joined')

    def get_roles(self, obj):
        # 取得與該使用者相關的所有角色
        return [role.name for role in obj.roles.all()]

    def get_module(self, obj):
        # 取得使用者的模組（假設每個使用者只有一個模組，透過使用者的角色取得模組）
        roles = obj.roles.all()
        if roles.exists():
            return roles[0].module.name
        return None


class RoleSerializer(serializers.ModelSerializer):
    module = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all())
    module_name = serializers.CharField(source='module.name', read_only=True) # 使用嵌套的 ModuleSerializer 來顯示模組詳細資訊
    users = UserSerializer(many=True, read_only=True)  # 假設 Role 和 User 是多對多關係

    class Meta:
        model = Role
        fields = ['id', 'name', 'is_active', 'module', 'users', 'module_name']
        extra_kwargs = {
            'name': {'required': True},
            'module': {'required': True},
            'users': {'required': True}
        }



class RolePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolePermission
        fields = ('id', 'role', 'permission_name', 'can_add', 'can_query', 'can_view', 'can_edit', 'can_delete', 'can_print', 'can_export', 'can_maintain', 'is_deleted')
        extra_kwargs = {
            'role': {'required': True},
            'permission_name': {'required': True}
        }

