<template>
  <div class="container">
    <div class="header">
      <button class="btn" @click="navigateToRoleManagement">角色</button>
      <button class="btn" @click="navigateToModuleManagement">模組</button>
    </div>
    <h2>角色管理</h2>
    <button id="add-role-btn" class="btn" @click="openCreateRoleModal">
      新增角色
    </button>
    <label for="chart-module-select">圖表模組:</label>
    <select id="chart-module-select" v-model="selectedModule" @change="filterRolesByModule">
      <option value="all">所有模組</option>
      <option v-for="module in modules" :key="module.id" :value="module.name">{{ module.name }}</option>
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
        <tr v-for="role in filteredRoles" :key="role.id" :data-module="role.module">
          <td>{{ role.name }}</td>
          <td>
            <button class="status-btn" @click="toggleStatus(role.id, !role.is_active)">
              {{ role.is_active ? '關閉' : '開啟' }}
            </button>
          </td>
          <td v-if="role.users">{{ role.users.length }}</td>
          <td v-else>0</td>
          <td>
            <select v-if="role.users">
              <option v-for="user in role.users" :key="user.id" :value="user.id">{{ user.username }}</option>
            </select>
          </td>
          <td>{{ role.module }}</td>
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
  </div>
</template>

<script>
import axios from '../axios';
import '../assets/RoleManagement.css';

export default {
  name: 'RoleManagement',
  data() {
    return {
      roles: [],
      modules: [],
      selectedModule: 'all',
      showCreateRoleModal: false,
      newRole: {
        name: '',
        module: ''
      }
    };
  },
  computed: {
    filteredRoles() {
      return this.roles.filter(role => {
        return this.selectedModule === 'all' || role.module === this.selectedModule;
      });
    }
  },
  methods: {
    async fetchRoles() {
      try {
        const response = await axios.get('/api/roles/');
        this.roles = response.data;
      } catch (error) {
        console.error('Error fetching roles:', error);
      }
    },
    async fetchModules() {
      try {
        const response = await axios.get('/api/modules/');
        this.modules = response.data;
      } catch (error) {
        console.error('Error fetching modules:', error);
      }
    },
    openCreateRoleModal() {
      this.showCreateRoleModal = true;
    },
    closeCreateRoleModal() {
      this.showCreateRoleModal = false;
    },
    createRole() {
      console.log('Creating role', this.newRole);
      this.closeCreateRoleModal();
    },
    filterRolesByModule() {
      console.log('Filtering roles by module', this.selectedModule);
    },
    toggleStatus(roleId, isActive) {
      console.log(`Toggling status for role ID: ${roleId}, isActive: ${isActive}`);
    },
    navigateToEditRole(roleId) {
      this.$router.push(`/edit_role/${roleId}`);
    },
    navigateToRoleManagement() {
      this.$router.push('/management/role-management');
    },
    navigateToModuleManagement() {
      this.$router.push('/management/module-management');
    },
    deleteRole(roleId) {
      console.log(`Deleting role with ID: ${roleId}`);
    }
  },
  mounted() {
    this.fetchRoles();
    this.fetchModules();
  }
};
</script>


<style scoped src="../assets/css/RoleManagement.css"></style>
