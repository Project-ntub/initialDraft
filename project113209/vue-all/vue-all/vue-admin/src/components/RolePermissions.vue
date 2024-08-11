<template>
  <div class="container">
    <h2>新增權限</h2>
    <form @submit.prevent="createPermission">
      <div class="form-group">
        <label for="permission-name">功能名稱</label>
        <input v-model="permissionName" id="permission-name" />
      </div>
      <div class="form-group">
        <label>權限</label>
        <div>
          <label><input type="checkbox" v-model="permissions.can_add" /> 新增</label>
          <label><input type="checkbox" v-model="permissions.can_query" /> 查詢</label>
          <label><input type="checkbox" v-model="permissions.can_view" /> 檢視</label>
          <label><input type="checkbox" v-model="permissions.can_edit" /> 修改</label>
          <label><input type="checkbox" v-model="permissions.can_delete" /> 刪除</label>
          <label><input type="checkbox" v-model="permissions.can_print" /> 列印</label>
          <label><input type="checkbox" v-model="permissions.can_export" /> 匯出</label>
          <label><input type="checkbox" v-model="permissions.can_maintain" /> 維護</label>
        </div>
      </div>
      <button type="submit" class="btn">新增</button>
      <button type="button" class="btn secondary" @click="navigateToEditRole">取消</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      permissionName: '',
      permissions: {
        can_add: false,
        can_query: false,
        can_view: false,
        can_edit: false,
        can_delete: false,
        can_print: false,
        can_export: false,
        can_maintain: false,
      }
    };
  },
  methods: {
    async createPermission() {
      try {
        const response = await axios.post(`/api/backend/role_permissions/`, {
          role: this.$route.params.roleId,
          permission_name: this.permissionName,
          ...this.permissions
        });
        if (response.data.success) {
          this.$router.push(`/management/edit_role/${this.$route.params.roleId}`);
        } else {
          alert("新增權限失敗");
        }
      } catch (error) {
        console.error('Error creating permission:', error.response ? error.response.data : error.message);
      }
    },
    navigateToEditRole() {
      this.$router.push(`/management/edit_role/${this.$route.params.roleId}`);
    }
  }
}
</script>


<style scoped src="../assets/css/RolePermissions.css"></style>
