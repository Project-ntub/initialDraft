<template>
    <div class="container">
      <div class="header">
        <div>
          <button class="btn" :class="{ active: currentPage === 'role_management' }" @click="navigateToRoleManagement">
            角色
          </button>
          <button class="btn" :class="{ active: currentPage === 'module_management' }" @click="navigateToModuleManagement">
            模組
          </button>
        </div>
      </div>
      <h2>角色管理</h2>
      <button id="add-role-btn" class="btn" @click="openCreateRoleModal">
        新增角色
      </button>
      <label for="chart-module-select">圖表模組:</label>
      <select id="chart-module-select" v-model="selectedModule" @change="filterRolesByModule">
        <option value="all">所有模組</option>
        <option v-for="module in modules" :key="module.name" :value="module.name">{{ module.name }}</option>
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
            <td>{{ role.users.length }}</td>
            <td>
              <select>
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
  
      <div id="create-role-modal" class="modal" v-if="showCreateRoleModal">
        <div class="modal-content">
          <span class="close" @click="closeCreateRoleModal">&times;</span>
          <h2>新增角色</h2>
          <form @submit.prevent="createRole">
            <div class="form-group">
              <label for="role-name">角色名稱</label>
              <input type="text" id="role-name" v-model="newRole.name" required />
            </div>
            <div class="form-group">
              <label for="role-module">模組</label>
              <select id="role-module" v-model="newRole.module" required>
                <option v-for="module in modules" :key="module.id" :value="module.name">{{ module.name }}</option>
              </select>
            </div>
            <button type="submit" class="btn">新增</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RoleManagement',
    data() {
      return {
        currentPage: 'role_management',
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
      navigateToRoleManagement() {
        this.currentPage = 'role_management';
        this.$router.push('/role_management');
      },
      navigateToModuleManagement() {
        this.currentPage = 'module_management';
        this.$router.push('/module_management');
      },
      openCreateRoleModal() {
        this.showCreateRoleModal = true;
      },
      closeCreateRoleModal() {
        this.showCreateRoleModal = false;
      },
      createRole() {
        // Implement your create role logic here
        console.log('Creating role', this.newRole);
        this.closeCreateRoleModal();
      },
      filterRolesByModule() {
        // Implement your filter logic here
        console.log('Filtering roles by module', this.selectedModule);
      },
      toggleStatus(roleId, isActive) {
        // Implement your toggle status logic here
        console.log(`Toggling status for role ID: ${roleId}, isActive: ${isActive}`);
      },
      navigateToEditRole(roleId) {
        this.$router.push(`/edit_role/${roleId}`);
      },
      deleteRole(roleId) {
        // Implement your delete role logic here
        console.log(`Deleting role with ID: ${roleId}`);
      }
    },
    mounted() {
      // Fetch the roles and modules from the backend or pass them as props
      this.roles = [
        // Sample data
        { id: 1, name: 'Admin', is_active: true, module: 'Module1', users: [{ id: 1, username: 'John' }, { id: 2, username: 'Jane' }] },
        // Add more sample roles here
      ];
      this.modules = [
        // Sample data
        { id: 1, name: 'Module1' },
        // Add more sample modules here
      ];
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
  