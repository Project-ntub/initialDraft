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
// import '../assets/Management.css';
import { ref, watch } from 'vue';
import { useRoute, useRouter } from 'vue-router';

export default {
  name: 'AppManagement',
  setup() {
    const isSidebarActive = ref(false);
    const route = useRoute();
    const router = useRouter();
    const hasRouteComponent = ref(false);

    watch(route, (newRoute) => {
      hasRouteComponent.value = newRoute.matched.length > 1;
    }, { immediate: true });

    const toggleSidebar = () => {
      isSidebarActive.value = !isSidebarActive.value;
    };

    const logout = () => {
      router.push('/login');
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

<style scoped src="../assets/css/Management.css"></style>
