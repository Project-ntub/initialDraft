<template>
  <div class="container">
    <div class="header">
      <button class="btn" @click="navigateToRoleManagement">角色</button>
      <button class="btn" @click="navigateToModuleManagement">模組</button>
    </div>
    <h2>模組管理</h2>
    <button id="add-module-btn" class="btn" @click="openCreateModuleModal">新增模組</button>
    <table class="module-table">
      <thead>
        <tr>
          <th>模組名稱</th>
          <th>用戶數</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="module in modules" :key="module.id">
          <td>{{ module.name }}</td>
          <td>{{ getUserCount(module.id) }}</td>
          <td>
            <button @click="openEditModuleModal(module.id, module.name)">編輯</button>
            <button @click="deleteModule(module.id)">刪除</button>
          </td>
        </tr>
      </tbody>
    </table>

    <ModuleForm v-if="showCreateModuleModal" @close="closeCreateModuleModal" @create="createModule" />
  </div>
</template>

<script>
import axios from 'axios';
import ModuleForm from './ModuleForm.vue';

export default {
  name: "ModuleManagement",
  components: {
    ModuleForm
  },
  data() {
    return {
      modules: [],
      users: [],
      showCreateModuleModal: false,
      newModuleName: "",
      editModuleName: "",
      editModuleId: null
    };
  },
  methods: {
    async loadModules() {
      try {
        const response = await axios.get('/api/backend/modules/');
        this.modules = response.data;
      } catch (error) {
        console.error('Error fetching modules:', error.response ? error.response.data : error.message);
      }
    },
    openCreateModuleModal() {
      this.showCreateModuleModal = true;
    },
    closeCreateModuleModal() {
      this.showCreateModuleModal = false;
    },
    async createModule(newModule) {
      try {
        const response = await axios.post('/api/backend/modules/', newModule);
        if (response.data.success) {
          this.loadModules();
          this.closeCreateModuleModal();
        } else {
          alert("新增模組失敗");
        }
      } catch (error) {
        console.error('Error creating module:', error.response ? error.response.data : error.message);
      }
    },
    openEditModuleModal(id, name) {
      this.editModuleId = id;
      this.editModuleName = name;
      this.showEditModuleModal = true;
    },
    closeEditModuleModal() {
      this.showEditModuleModal = false;
    },
    async editModule() {
      try {
        const response = await axios.put(`/api/backend/modules/${this.editModuleId}/`, { name: this.editModuleName });
        if (response.data.success) {
          this.loadModules();
          this.closeEditModuleModal();
        } else {
          alert("編輯模組失敗");
        }
      } catch (error) {
        console.error('Error editing module:', error.response ? error.response.data : error.message);
      }
    },
    async deleteModule(id) {
      try {
        const response = await axios.delete(`/api/backend/modules/${id}/`);
        if (response.data.success) {
          this.loadModules();
        } else {
          alert("刪除模組失敗");
        }
      } catch (error) {
        console.error('Error deleting module:', error.response ? error.response.data : error.message);
        alert("刪除模組失敗");
      }
    },
    navigateToRoleManagement() {
      this.$router.push('/management/role-management');
    },
    navigateToModuleManagement() {
      this.$router.push('/management/module-management');
    },
    getUserCount(moduleId) {
      return this.users.filter(user => user.module.id === moduleId).length;
    }
  },
  async mounted() {
    await this.loadModules();
    try {
      const response = await axios.get('/api/backend/users/');
      this.users = response.data;
    } catch (error) {
      console.error('Error fetching users:', error.response ? error.response.data : error.message);
    }
  }
};
</script>

<style scoped src="../assets/css/ModuleManagement.css"></style>
