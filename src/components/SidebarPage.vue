<template>
  <div class="sidebar" ref="sidebar">
    <div class="sidebar-header">
      <font-awesome-icon icon="user" class="icon" />
      <span>王曉明</span>
      <span class="toggle-btn" @click="toggleSidebar">☰</span>
    </div>
    <router-link to="/home">
      <font-awesome-icon icon="tachometer-alt" class="icon" />
      <span class="text">儀錶板管理</span>
    </router-link>
    <router-link to="/profile">
      <font-awesome-icon icon="user" class="icon" />
      <span class="text">個人資訊</span>
    </router-link>
    <router-link to="/accountsettings">
      <font-awesome-icon icon="users" class="icon" />
      <span class="text">帳號設定</span>
    </router-link>
    <router-link to="/history">
      <font-awesome-icon icon="history" class="icon" />
      <span class="text">歷史紀錄</span>
    </router-link>
    <a href="#" @click.prevent="confirmLogout">
      <font-awesome-icon icon="sign-out-alt" class="icon" />
      <span class="text">登出</span>
    </a>

    <div :class="['content', { shift: isSidebarOpen }]">
      <slot></slot>
    </div>
  </div>

</template>

<script>
export default {
  name: "SidebarPage",
  methods: {
    toggleSidebar() {
      const sidebar = this.$refs.sidebar;
      if (sidebar) {
        sidebar.classList.toggle("open");
      }
      const content = document.getElementById("content");
      if (content) {
        content.classList.toggle("shift");
      }
    },
    confirmLogout() {
      const confirmed = confirm("確定要登出嗎？");
      if (confirmed) {
        this.logout();
      }
    },
    logout() {
      alert("已登出");
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped src="../assets/css/SidebarPage.css"></style>
