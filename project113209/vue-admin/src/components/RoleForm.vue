<template>
  <div class="container">
    <h2>{{ isEdit ? "編輯角色" : "新增角色" }}</h2>
    <form @submit.prevent="saveRole">
      <div class="form-group">
        <label for="role-name">角色名稱</label>
        <input type="text" v-model="localRole.name" id="role-name" required />
      </div>
      <div class="form-group">
        <label for="role-users">角色成員</label>
        <input type="text" v-model="localRole.users" id="role-users" />
      </div>
      <div class="form-group">
        <label for="role-is-active">角色狀態</label>
        <input type="checkbox" v-model="localRole.isActive" id="role-is-active" />
      </div>
      <div class="form-group">
        <label for="role-module">模組</label>
        <input type="text" v-model="localRole.module" id="role-module" />
      </div>
      <div v-if="isEdit" class="form-group">
        <label>角色權限</label>
        <table>
          <thead>
            <tr>
              <th>功能</th>
              <th>新增</th>
              <th>查詢</th>
              <th>檢視</th>
              <th>修改</th>
              <th>刪除</th>
              <th>列印</th>
              <th>匯出</th>
              <th>維護</th>
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="permission in localRolePermissions" :key="permission.id">
              <td>{{ permission.permissionName }}</td>
              <td><input type="checkbox" v-model="permission.canAdd" /></td>
              <td><input type="checkbox" v-model="permission.canQuery" /></td>
              <td><input type="checkbox" v-model="permission.canView" /></td>
              <td><input type="checkbox" v-model="permission.canEdit" /></td>
              <td><input type="checkbox" v-model="permission.canDelete" /></td>
              <td><input type="checkbox" v-model="permission.canPrint" /></td>
              <td><input type="checkbox" v-model="permission.canExport" /></td>
              <td><input type="checkbox" v-model="permission.canMaintain" /></td>
              <td>
                <button type="button" @click="deletePermission(permission.id)">刪除</button>
              </td>
            </tr>
          </tbody>
        </table>
        <button type="button" @click="addPermission">新增權限</button>
      </div>
      <button type="submit" class="btn">{{ isEdit ? "保存變更" : "新增" }}</button>
      <button type="button" class="btn secondary" @click="cancel">取消</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: "RoleForm",
  data() {
    return {
      localRole: {
        name: '',
        module: ''
      },
      localRolePermissions: [],
      isEdit: false,
      modules: [] // 添加模块数据
    };
  },
  methods: {
    async saveRole() {
      try {
        const response = this.isEdit
          ? await axios.put(`/api/backend/roles/${this.localRole.id}/`, {
              role: this.localRole,
              role_permissions: this.localRolePermissions
            })
          : await axios.post("/api/backend/roles/", {
              role: this.localRole,
              role_permissions: this.localRolePermissions
            });
        if (response.data.success) {
          alert("保存成功");
          this.$router.push({ name: 'roleManagement' });
        } else {
          alert("保存失敗");
        }
      } catch (error) {
        console.error('Error saving role:', error.response ? error.response.data : error.message);
        alert("保存失敗");
      }
    },
    deletePermission(permissionId) {
      this.localRolePermissions = this.localRolePermissions.filter(p => p.id !== permissionId);
    },
    addPermission() {
      if (!Array.isArray(this.localRolePermissions)) {
        this.localRolePermissions = [];
      }
      this.localRolePermissions.push({
        id: Date.now(), // You should replace this with a more robust ID generation in production
        permissionName: '',
        canAdd: false,
        canQuery: false,
        canView: false,
        canEdit: false,
        canDelete: false,
        canPrint: false,
        canExport: false,
        canMaintain: false
      });
    },
    cancel() {
      this.$router.go(-1);
    },
    async loadRole(roleId) {
      try {
        const response = await axios.get(`/api/backend/roles/${roleId}/`);
        this.localRole = response.data;
        this.localRolePermissions = response.data.permissions;
      } catch (error) {
        console.error('Error loading role:', error.response ? error.response.data : error.message);
      }
    },
    async fetchModules() {
      try {
        const response = await axios.get('/api/backend/modules/');
        this.modules = response.data;
      } catch (error) {
        console.error('Error fetching modules:', error);
      }
    }
  },
  async mounted() {
    const roleId = this.$route.params.roleId;
    await this.fetchModules(); // 确保在加载组件时获取模块数据
    if (roleId) {
      this.isEdit = true;
      await this.loadRole(roleId);
    }
  }
};
</script>

<style scoped src="../assets/css/RoleForm.css"></style>
