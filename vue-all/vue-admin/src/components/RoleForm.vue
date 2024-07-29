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
        <div class="member-container">
          <div v-for="(userId, index) in localRole.users" :key="index" class="member-item">
            <select v-model="localRole.users[index]" @change="updateMembers">
              <option value="">-- 選擇成員 --</option>
              <option v-for="user in filteredUsers" :key="user.id" :value="user.id">{{ user.username }}</option>
            </select>
            <button type="button" @click="removeMember(index)">-</button>
          </div>
          <button type="button" @click="addMember">+</button>
        </div>
      </div>
      <div class="form-group">
        <label for="role-is-active">角色狀態</label>
        <input type="checkbox" v-model="localRole.is_active" id="role-is-active" />
      </div>
      <div class="form-group">
        <label for="role-module">模組</label>
        <select v-model="localRole.module" id="role-module">
          <option value="">-- 選擇模組 --</option>
          <option v-for="module in availableModules" :key="module.id" :value="module.id">{{ module.name }}</option>
        </select>
      </div>
      <div class="form-group">
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
            <tr v-for="permission in rolePermissions" :key="permission.id">
              <td>{{ permission.permission_name }}</td>
              <td><input type="checkbox" v-model="permission.can_add" /></td>
              <td><input type="checkbox" v-model="permission.can_query" /></td>
              <td><input type="checkbox" v-model="permission.can_view" /></td>
              <td><input type="checkbox" v-model="permission.can_edit" /></td>
              <td><input type="checkbox" v-model="permission.can_delete" /></td>
              <td><input type="checkbox" v-model="permission.can_print" /></td>
              <td><input type="checkbox" v-model="permission.can_export" /></td>
              <td><input type="checkbox" v-model="permission.can_maintain" /></td>
              <td>
                <button type="button" @click="deletePermission(permission.id)">刪除</button>
              </td>
            </tr>
          </tbody>
        </table>
        <button type="button" @click="navigateToAddPermission">新增權限</button>
      </div>
      <button type="submit" class="btn">{{ isEdit ? "保存變更" : "新增" }}</button>
      <button type="button" class="btn secondary" @click="cancel">取消</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "RoleForm",
  data() {
    return {
      localRole: {
        name: '',
        module: '',
        users: [],
        is_active: false
      },
      availableUsers: [],
      availableModules: [],
      rolePermissions: [],
      isEdit: false
    };
  },
  computed: {
    filteredUsers() {
      const selectedUserIds = new Set(this.localRole.users);
      return this.availableUsers.filter(user => !selectedUserIds.has(user.id));
    }
  },
  methods: {
    async saveRole() {
      try {
        const roleData = {
          ...this.localRole,
          users: this.localRole.users.map(user => user.id) // Ensure we send only user IDs
        };
        const response = this.isEdit
          ? await axios.put(`/api/backend/roles/${this.localRole.id}/`, roleData)
          : await axios.post("/api/backend/roles/", roleData);
        if (response.status === 200 || response.status === 201) {
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
    async fetchUsers() {
      try {
        const response = await axios.get('/api/backend/users/');
        this.availableUsers = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    async fetchModules() {
      try {
        const response = await axios.get('/api/backend/modules/');
        this.availableModules = response.data;
      } catch (error) {
        console.error('Error fetching modules:', error);
      }
    },
    addMember() {
      this.localRole.users.push('');
    },
    removeMember(index) {
      this.localRole.users.splice(index, 1);
    },
    updateMembers() {
      this.$forceUpdate();
    },
    cancel() {
      this.$router.push({ name: 'roleManagement' });
    },
    async fetchRolePermissions(roleId) {
      try {
        const response = await axios.get(`/api/backend/role_permissions/?role=${roleId}`);
        this.rolePermissions = response.data;
      } catch (error) {
        console.error('Error fetching role permissions:', error);
      }
    },
    navigateToAddPermission() {
      this.$router.push(`/management/role_permissions/${this.localRole.id}`);
    },
    async loadRole(roleId) {
      try {
        const response = await axios.get(`/api/backend/roles/${roleId}/`);
        const role = response.data;
        this.localRole = {
          id: role.id,
          name: role.name,
          module: role.module.id, // Ensure module ID is used
          users: role.users.map(user => user.id), // Ensure only user IDs are used
          is_active: role.is_active
        };
        await this.fetchRolePermissions(roleId);
        this.updateMembers();
      } catch (error) {
        console.error('Error loading role:', error.response ? error.response.data : error.message);
      }
    }
  },
  async mounted() {
    const roleId = this.$route.params.roleId;
    await this.fetchUsers();
    await this.fetchModules();
    if (roleId) {
      this.isEdit = true;
      await this.loadRole(roleId);
    }
  }
};
</script>

<style scoped src="../assets/css/RoleForm.css"></style>
