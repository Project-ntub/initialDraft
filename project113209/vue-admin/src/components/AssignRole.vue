<template>
  <div class="container">
    <h2>分配角色和模組給 {{ user.username }}</h2>
    <form @submit.prevent="assignRoleAndModule">
      <label for="module">選擇模組:</label>
      <select id="module" v-model="selectedModule" @change="loadRoles">
        <option value="">-- 選擇模組 --</option>
        <option v-for="module in modules" :key="module.id" :value="module.id">
          {{ module.name }}
        </option>
      </select>
      <label for="role">選擇角色:</label>
      <select id="role" v-model="selectedRole">
        <option value="">-- 選擇角色 --</option>
        <option v-for="role in roles" :key="role.id" :value="role.id">
          {{ role.name }}
        </option>
      </select>
      <button type="submit">保存</button>
    </form>
    <button @click="goBack">回到上一頁</button>
  </div>
</template>

<script>
export default {
  name: "AssignRoleAndModule",
  data() {
    return {
      selectedModule: "",
      selectedRole: "",
      modules: [],
      roles: [],
      user: { username: "user" } // 假設用戶數據
    };
  },
  methods: {
    loadModules() {
      // 加載模組數據
      this.$http.get("/backend/modules")
        .then(response => {
          this.modules = response.data.modules;
        });
    },
    loadRoles() {
      if (this.selectedModule) {
        this.$http.get(`/backend/get_roles_by_module/${this.selectedModule}/`)
          .then(response => {
            this.roles = response.data.roles;
          });
      } else {
        this.roles = [];
      }
    },
    assignRoleAndModule() {
      // 發送請求到後端
      this.$http.post("/backend/assign_role_and_module", {
        module: this.selectedModule,
        role: this.selectedRole
      }).then(response => {
        if (response.data.success) {
          alert("保存成功");
        } else {
          alert("保存失敗");
        }
      });
    },
    goBack() {
      this.$router.go(-1);
    }
  },
  mounted() {
    this.loadModules();
  }
};
</script>

<style scoped src="../assets/css/AssignRole.css"></style>
