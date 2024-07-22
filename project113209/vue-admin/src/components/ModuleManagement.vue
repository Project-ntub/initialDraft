<template>
  <div class="container">
    <div class="header">
      <button class="btn" @click="navigateToRoleManagement">角色</button>
      <button class="btn" @click="navigateToModuleManagement">模組</button>
    </div>
    <h2>模組管理</h2>
    <button id="add-module-btn" class="btn" @click="openCreateModuleModal">
      新增模組
    </button>
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
          <td>{{ module.user_count }}</td>
          <td>
            <button @click="openEditModuleModal(module.id, module.name)">編輯</button>
            <button @click="deleteModule(module.id)">刪除</button>
          </td>
        </tr>
      </tbody>
    </table>

    <div v-if="showCreateModuleModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeCreateModuleModal">&times;</span>
        <h2>新增模組</h2>
        <form @submit.prevent="createModule">
          <div class="form-group">
            <label for="module-name">模組名稱</label>
            <input type="text" v-model="newModuleName" id="module-name" required />
          </div>
          <button type="submit" class="btn">新增</button>
        </form>
      </div>
    </div>

    <div v-if="showEditModuleModal" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeEditModuleModal">&times;</span>
        <h2>編輯模組</h2>
        <form @submit.prevent="editModule">
          <div class="form-group">
            <label for="edit-module-name">模組名稱</label>
            <input type="text" v-model="editModuleName" id="edit-module-name" required />
          </div>
          <button type="submit" class="btn">保存</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: "ModuleManagement",
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
    navigateToRoleManagement() {
      this.$router.push({ name: 'roleManagement' });
    },
    navigateToModuleManagement() {
      this.$router.push({ name: 'moduleManagement' });
    },
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
    async createModule() {
      try {
        const response = await axios.post('/api/backend/modules/', { name: this.newModuleName });
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
      }
    }
  },
  mounted() {
    this.loadModules();
  }
};
</script>

<style scoped src="../assets/css/ModuleManagement.css"></style>
