from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'department_id', 'position_id', 'branch_id', 'module', 'gender')
    search_fields = ('username', 'email', 'phone')  # 允許管理員在後台搜索這些字段
    list_filter = ('department_id', 'position_id', 'branch_id', 'gender')  # 在側邊添加過濾器，方便查找
