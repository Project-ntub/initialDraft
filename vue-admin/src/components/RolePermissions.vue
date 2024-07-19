<template>
  <div class="container">
    <h2>角色權限管理</h2>
    <form @submit.prevent="submitPermissions">
      <div class="form-group">
        <label for="role-name">角色名稱:</label>
        <select v-model="selectedRole">
          <option value="store-manager">店長</option>
          <!-- 其他角色選項 -->
        </select>
      </div>
      <div class="form-group">
        <label for="module-select">模組選擇:</label>
        <select v-model="selectedModule">
          <option value="revenue-analysis">營業額分析模組</option>
          <option value="inventory-management">庫存管理模組</option>
          <option value="sales-management">銷售額分析模組</option>
        </select>
      </div>
      <div class="form-group">
        <label>功能:</label>
        <div v-for="functionItem in functions" :key="functionItem.id">
          <input type="checkbox" :id="functionItem.id" :value="functionItem.id" v-model="selectedFunctions" />
          <label :for="functionItem.id">{{ functionItem.label }}</label>
        </div>
      </div>
      <div class="form-group">
        <label>權限:</label>
        <div v-for="permission in permissions" :key="permission.id">
          <input type="checkbox" :id="permission.id" :value="permission.id" v-model="selectedPermissions" />
          <label :for="permission.id">{{ permission.label }}</label>
        </div>
      </div>
      <div class="form-buttons">
        <button type="submit" class="submit-btn">提交</button>
        <button type="button" class="cancel-btn" @click="cancel">取消</button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "RolePermissions",
  data() {
    return {
      selectedRole: "",
      selectedModule: "",
      selectedFunctions: [],
      selectedPermissions: [],
      functions: [
        { id: "daily-revenue-report", label: "查看日營業額報告" },
        { id: "monthly-trend", label: "查看月度趨勢" }
      ],
      permissions: [
        { id: "view", label: "查看" },
        { id: "export", label: "匯出" }
      ]
    };
  },
  methods: {
    submitPermissions() {
      // 發送請求到後端
      this.$http.post("/backend/role_permissions", {
        role: this.selectedRole,
        module: this.selectedModule,
        functions: this.selectedFunctions,
        permissions: this.selectedPermissions
      }).then(response => {
        if (response.data.success) {
          alert("保存成功");
        } else {
          alert("保存失敗");
        }
      });
    },
    cancel() {
      this.$router.go(-1);
    }
  }
};
</script>

<style scoped src="../assets/css/RolePermissions.css"></style>
