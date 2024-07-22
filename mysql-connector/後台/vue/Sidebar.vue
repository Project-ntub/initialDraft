<!-- src/components/Sidebar.vue -->
<template>
    <div :class="['sidebar', { collapsed: isCollapsed }]">
      <h2>管理介面</h2>
      <router-link to="/dashboard">儀錶板管理</router-link>
      <router-link to="/user-management">用戶管理</router-link>
      <router-link to="/role-management">角色管理</router-link>
      <router-link to="/history">歷史紀錄</router-link>
      <router-link to="/preferences">個人偏好</router-link>
      <router-link to="/profile">個人資料</router-link>
      <button class="logout-btn" @click="logout">登出</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isCollapsed: false
      };
    },
    methods: {
      logout() {
        this.$router.push('/logout-success');
      }
    }
  };
  </script>
  
  <style scoped>
  /* 包含你在原始 HTML 中的 CSS */
  </style>
  