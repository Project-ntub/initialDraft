<template>
  <div>
    <div class="hamburger-menu" @click="toggleSidebar">
      <div class="hamburger-icon">☰</div>
    </div>
    <div class="sidebar" :class="{ active: isSidebarActive }">
      <h2>管理介面</h2>
      <router-link to="/management/dashboard">儀錶板管理</router-link>
      <router-link to="/management/user-management">用戶管理</router-link>
      <router-link to="/management/role-management">角色管理</router-link>
      <router-link to="/management/history">歷史紀錄</router-link>
      <button class="logout-btn" @click="logout">登出</button>
    </div>
    <div class="main-content" :class="{ shifted: isSidebarActive }" id="main-content">
      <router-view v-slot="{ Component }">
        <component :is="Component" v-if="Component" />
      </router-view>
      <div v-if="!hasRouteComponent">
        <h1 id="welcome-title">歡迎來到管理介面</h1>
        <p id="welcome-description">請選擇一個選項來管理。</p>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';

export default {
  name: 'AppManagement',
  setup() {
    const isSidebarActive = ref(false);
    const route = useRoute();
    const hasRouteComponent = ref(false);

    watch(route, (newRoute) => {
      hasRouteComponent.value = newRoute.matched.length > 1;
    }, { immediate: true });

    const toggleSidebar = () => {
      isSidebarActive.value = !isSidebarActive.value;
    };

    const logout = () => {
      // 這裡可以實現登出邏輯
      this.$router.push('/login');
    };

    return {
      isSidebarActive,
      toggleSidebar,
      logout,
      hasRouteComponent,
    };
  }
};
</script>

<style scoped>
/* 添加CSS樣式 */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  height: 100vh;
  background-color: #f4f4f4;
}

.hamburger-menu {
  position: fixed;
  top: 10px;
  left: 10px;
  z-index: 1000;
  cursor: pointer;
}

.hamburger-icon {
  font-size: 30px;
}

.sidebar {
  width: 250px;
  background-color: #333;
  color: #fff;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding-top: 20px;
  position: fixed;
  top: 0;
  left: -250px;
  height: 100%;
  transition: left 0.3s ease;
}

.sidebar.active {
  left: 0;
}

.sidebar h2 {
  margin-left: 20px;
  margin-bottom: 20px;
}

.sidebar a {
  text-decoration: none;
  color: #fff;
  margin: 10px 0;
  padding: 10px 20px;
  width: 100%;
  text-align: left;
  background-color: #333;
  border-radius: 0;
  display: block;
  transition: background-color 0.3s;
  box-sizing: border-box;
}

.sidebar a:hover {
  background-color: #444;
}

.main-content {
  flex: 1;
  padding: 60px 20px 20px 20px;
  margin-left: 0;
  transition: margin-left 0.3s ease;
}

.main-content.shifted {
  margin-left: 250px;
}

.logout-btn {
  margin-top: auto;
  margin-bottom: 20px;
  padding: 10px 20px;
  background-color: #e74c3c;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
  width: 100%;
  text-align: left;
  box-sizing: border-box;
}

.logout-btn:hover {
  background-color: #c0392b;
}
</style>
