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


<style scoped>
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.container {
    width: 90%;
    margin: 20px auto;
    background-color: #ffffff;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
}

.header {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-bottom: 20px;
    flex-wrap: wrap;
}

.header button {
    margin-right: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    background-color: #6c757d;
    color: white;
    font-size: 16px;
}

.header button.active {
    background-color: #007bff;
}

.header button:hover {
    background-color: #5a6268;
}

.header h2 {
    margin: 0;
    padding-top: 10px;
    flex-grow: 1;
}

.role-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
}

.role-table th, .role-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

.role-table th {
    background-color: #f2f2f2;
}

.role-table tr:nth-child(even) {
    background-color: #f9f9f9;
}

.role-table tr:hover {
    background-color: #ddd;
}

.status-btn {
    padding: 8px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    color: white;
    font-size: 14px;
    margin: 2px;
    background-color: #007bff;
}

.status-btn:hover {
    background-color: #0056b3;
}

.permissions-btn {
    padding: 8px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    color: white;
    font-size: 14px;
    margin: 2px;
    background-color: #28a745;
}

.permissions-btn:hover {
    background-color: #218838;
}

.delete-btn {
    padding: 8px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    color: white;
    font-size: 14px;
    margin: 2px;
    background-color: #dc3545;
}

.delete-btn:hover {
    background-color: #c82333;
}

.modal {
    display: none;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0, 0, 0, 0.4);
    padding-top: 60px;
}

.modal-content {
    background-color: #fefefe;
    margin: 5% auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
}

.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input[type="text"], input[type="checkbox"], select {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
    margin-top: 5px;
}

#add-role-btn {
    margin-top: 20px;
    margin-bottom: 20px;
}

#chart-module-select {
    margin-top: 20px;
}

select {
    cursor: pointer;
}

@media (max-width: 768px) {
    .header {
        flex-direction: column;
        align-items: flex-start;
    }

    .header button, .header h2 {
        width: 100%;
        text-align: center;
        margin: 5px 0;
    }

    .status-btn, .permissions-btn, .delete-btn {
        width: 100%;
        margin: 5px 0;
    }
}

</style>
