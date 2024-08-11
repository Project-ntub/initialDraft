<template>
  <div class="container">
    <div class="header">
      <button class="btn" @click="navigateToRoleManagement">角色</button>
      <button class="btn" @click="navigateToModuleManagement">模組</button>
    </div>
    <h2>角色管理</h2>
    <button id="add-role-btn" class="btn" @click="openCreateRoleModal">新增角色</button>
    <label for="chart-module-select">圖表模組:</label>
    <select id="chart-module-select" v-model="selectedModule" @change="filterRolesByModule">
      <option value="all">所有模組</option>
      <option v-for="module in modules" :key="module.id" :value="module.id">{{ module.name }}</option>
    </select>
    <table class="role-table">
      <thead>
        <tr>
          <th>角色名稱</th>
          <th>角色狀態</th>
          <th>用戶數</th>
          <th>角色成員</th>
          <th>模組</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody id="role-tbody">
        <tr v-for="role in filteredRoles" :key="role.id" :data-module="role.module.id">
          <td>{{ role.name }}</td>
          <td>
            <button class="status-btn" @click="toggleStatus(role.id, !role.is_active)">
              {{ role.is_active ? '關閉' : '開啟' }}
            </button>
          </td>
          <td>{{ role.users.length }}</td>
          <td>
            <select>
              <option v-for="user in role.users" :key="user.id" :value="user.id">{{ user.username }}</option>
            </select>
          </td>
          <td>{{ role.module ? role.module.name : '未知模組' }}</td>
          <td>
            <button class="permissions-btn" @click="navigateToEditRole(role.id)">
              角色權限
            </button>
            <button class="delete-btn" @click="deleteRole(role.id)">
              刪除
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <RoleForm v-if="showCreateRoleModal" :modules="modules" :users="users" @close="closeCreateRoleModal" @create="createRole" />
  </div>
</template>

<script>
import axios from 'axios';
import RoleForm from './RoleForm.vue';

export default {
  name: 'RoleManagement',
  components: {
    RoleForm
  },
  data() {
    return {
      roles: [],
      modules: [],
      users: [],
      selectedModule: 'all',
      showCreateRoleModal: false,
      newRole: {
        name: '',
        module: '',
        members: []
      }
    };
  },
  computed: {
    filteredRoles() {
      return this.roles.filter(role => {
        return this.selectedModule === 'all' || role.module.id === this.selectedModule;
      });
    }
  },
  methods: {
    async fetchRoles() {
      try {
        const response = await axios.get('/api/backend/roles/');
        this.roles = response.data;
      } catch (error) {
        console.error('Error fetching roles:', error);
      }
    },
    async fetchModules() {
      try {
        const response = await axios.get('/api/backend/modules/');
        this.modules = response.data;
      } catch (error) {
        console.error('Error fetching modules:', error);
      }
    },
    async fetchUsers() {
      try {
        const response = await axios.get('/api/backend/users/');
        this.users = response.data;
      } catch (error) {
        console.error('Error fetching users:', error);
      }
    },
    openCreateRoleModal() {
      this.showCreateRoleModal = true;
    },
    closeCreateRoleModal() {
      this.showCreateRoleModal = false;
    },
    async createRole(roleData) {
      try {
        const response = await axios.post('/api/backend/roles/', {
          role: roleData,
          role_permissions: []
        });
        if (response.status === 201) {
          this.fetchRoles();  // Reload roles data
          this.closeCreateRoleModal();
        } else {
          alert(response.data.message || "新增角色失敗");
        }
      } catch (error) {
        console.error("新增角色出現錯誤:", error);
        alert("新增角色時出現錯誤");
      }
    },
    filterRolesByModule() {
      console.log('Filtering roles by module', this.selectedModule);
    },
    async toggleStatus(roleId, isActive) {
      try {
        const response = await axios.post(`/api/backend/toggle_role_status/${roleId}/`, {
          is_active: isActive
        });
        if (response.data.success) {
          this.fetchRoles(); // Reload roles list
        } else {
          alert('切換狀態失敗');
        }
      } catch (error) {
        console.error('Error toggling status:', error);
        alert('切換狀態失敗');
      }
    },
    navigateToEditRole(roleId) {
      this.$router.push({ name: 'editRole', params: { roleId } });
    },
    navigateToRoleManagement() {
      this.$router.push('/management/role-management');
    },
    navigateToModuleManagement() {
      this.$router.push('/management/module-management');
    },
    async deleteRole(roleId) {
      try {
        const response = await axios.post(`/api/backend/delete_role/${roleId}/`);
        if (response.status === 204) {
          this.fetchRoles(); // Reload roles list
        } else {
          alert('刪除角色失敗');
        }
      } catch (error) {
        console.error('Error deleting role:', error);
        alert('刪除角色失敗');
      }
    }
  },
  mounted() {
    this.fetchRoles();
    this.fetchModules();
    this.fetchUsers();
  }
};
</script>

<style scoped src="../assets/css/RoleManagement.css"></style>
