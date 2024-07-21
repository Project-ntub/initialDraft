<template>
    <div class="container">
      <div class="header">
        <button @click="goToRoleManagement" :class="{ active: currentPage === 'role_management' }">角色</button>
        <button @click="goToModuleManagement" :class="{ active: currentPage === 'module_management' }">模組</button>
      </div>
      <h2>模組管理</h2>
      <button id="add-module-btn" @click="openCreateModuleModal">新增模組</button>
      <table class="module-table">
        <thead>
          <tr>
            <th>模組名稱</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="module in modules" :key="module.id">
            <td>{{ module.name }}</td>
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
  export default {
    name: "ModuleManagement",
    data() {
      return {
        currentPage: "module_management",
        modules: [],
        showCreateModuleModal: false,
        showEditModuleModal: false,
        newModuleName: "",
        editModuleName: "",
        editModuleId: null
      };
    },
    methods: {
      goToRoleManagement() {
        this.$router.push({ name: 'roleManagement' });
      },
      goToModuleManagement() {
        this.$router.push({ name: 'moduleManagement' });
      },
      loadModules() {
        // 加載模組數據
        this.$http.get("/backend/modules")
          .then(response => {
            this.modules = response.data.modules;
          });
      },
      openCreateModuleModal() {
        this.showCreateModuleModal = true;
      },
      closeCreateModuleModal() {
        this.showCreateModuleModal = false;
      },
      createModule() {
        // 發送請求到後端
        this.$http.post("/backend/create_module", { module_name: this.newModuleName })
          .then(response => {
            if (response.data.success) {
              this.loadModules();
              this.closeCreateModuleModal();
            } else {
              alert("新增模組失敗");
            }
          });
      },
      openEditModuleModal(id, name) {
        this.editModuleId = id;
        this.editModuleName = name;
        this.showEditModuleModal = true;
      },
      closeEditModuleModal() {
        this.showEditModuleModal = false;
      },
      editModule() {
        // 發送請求到後端
        this.$http.post("/backend/edit_module", { module_id: this.editModuleId, module_name: this.editModuleName })
          .then(response => {
            if (response.data.success) {
              this.loadModules();
              this.closeEditModuleModal();
            } else {
              alert("編輯模組失敗");
            }
          });
      },
      deleteModule(id) {
        // 發送刪除請求到後端
        this.$http.post(`/backend/delete_module/${id}`)
          .then(response => {
            if (response.data.success) {
              this.loadModules();
            } else {
              alert("刪除模組失敗");
            }
          });
      }
    },
    mounted() {
      this.loadModules();
    }
  };
  </script>
  
  <style scoped src="../assets/css/ModuleManagement.css"></style>

  