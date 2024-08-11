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
    <ModuleForm v-if="showEditModuleModal" :moduleId="editModuleId" :moduleName="editModuleName" @close="closeEditModuleModal" @edit="editModule" />
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
      showCreateModuleModal: false,
      showEditModuleModal: false,
      newModuleName: "",
      editModuleName: "",
      editModuleId: null
    };
  },
  methods: {
    async loadModules() {
      try {
        const response = await axios.get('/api/backend/modules/');
        console.log('Modules from backend:', response.data);  // 打印前端接收的數據
        this.modules = response.data.filter(module => !module.is_deleted) || [];
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
        if (response.status === 201) { // 201 Created
          this.loadModules();
          this.closeCreateModuleModal();
          alert("新增模組成功");
        } else {
          alert("新增模組失敗");
        }
      } catch (error) {
        console.error('Error creating module:', error.response ? error.response.data : error.message);
        alert("新增模組失敗");
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
    async editModule(updatedModule) {
      try {
        const response = await axios.put(`/api/backend/modules/${this.editModuleId}/`, updatedModule);
        if (response.status === 200) { // 200 OK
          this.loadModules();
          this.closeEditModuleModal();
          alert("編輯模組成功");
        } else {
          alert("編輯模組失敗");
        }
      } catch (error) {
        console.error('Error editing module:', error.response ? error.response.data : error.message);
        alert("編輯模組失敗");
      }
    },
    async deleteModule(id) { 
      try { 
        const response = await axios.delete(`/api/backend/modules/${id}/`); 
        console.log('Delete response:', response);  // 打印刪除響應
        if (response.status === 204) { 
          this.loadModules(); 
          alert("刪除成功");
        } else { 
          alert("刪除模組失敗"); 
          console.error('Error deleting module:', response.data.message); 
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
      const module = this.modules.find(m => m.id === moduleId);
      return module ? module.user_count : 0; // 確保返回值總是一个數字
    }
  },
  created() {
    this.loadModules();
  }
};
</script>

<style scoped src="../assets/css/ModuleManagement.css"></style>
