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
        <option v-for="role in roles" :key="role.id">
          {{ role.name }}
        </option>
      </select>
      <button type="submit">保存</button>
    </form>
    <button @click="goBack">回到上一頁</button>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: "AssignRoleAndModule",
  data() {
    return {
      selectedModule: "",
      selectedRole: "",
      modules: [],
      roles: [],
      user: {} // Initialize user as an empty object
    };
  },
  methods: {
    loadModules() {
      axios.get("/api/backend/get_modules/")
        .then(response => {
          this.modules = response.data.modules;
        })
        .catch(error => {
          console.error('Error loading modules:', error);
        });
    },
    loadRoles() {
      if (this.selectedModule) {
        axios.get(`/api/backend/get_roles_by_module/${this.selectedModule}/`)
          .then(response => {
            this.roles = response.data;
          })
          .catch(error => {
            console.error('Error loading roles:', error);
          });
      } else {
        this.roles = [];
      }
    },
    assignRoleAndModule() {
      const userId = this.$route.params.userId;
      axios.post(`/api/backend/assign_role_and_module/${userId}/`, {
        module: this.selectedModule,
        role: this.selectedRole
      }).then(response => {
        if (response.data.success) {
          alert("保存成功");
          this.$router.push({ name: 'userManagement' });
        } else {
          alert("保存失敗");
        }
      }).catch(error => {
        console.error('Error saving role and module:', error);
        alert("保存失敗");
      });
    },
    goBack() {
      this.$router.go(-1);
    },
    loadUser() {
      const userId = this.$route.params.userId;
      axios.get(`/api/backend/users/${userId}/`)
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          console.error('Error loading user:', error);
        });
    }
  },
  mounted() {
    this.loadModules();
    this.loadUser();
  }
};
</script>

<style scoped src="../assets/css/AssignRole.css"></style>
