<template>
    <div>
      <div class="hamburger-menu" @click="toggleSidebar">
        <div class="hamburger-icon">☰</div>
      </div>
      <div class="sidebar" :class="{ active: isSidebarActive }">
        <h2>管理介面</h2>
        <router-link to="/dashboard">儀錶板管理</router-link>
        <router-link to="/user-management">用戶管理</router-link>
        <router-link to="/role-management">角色管理</router-link>
        <router-link to="/history">歷史紀錄</router-link>
        <button class="logout-btn" @click="logout">登出</button>
      </div>
      <div class="main-content" :class="{ shifted: isSidebarActive }" id="main-content">
        <router-view />
      </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'AppManagement',
    data() {
      return {
        isSidebarActive: false,
      };
    },
    methods: {
      toggleSidebar() {
        this.isSidebarActive = !this.isSidebarActive;
      },
      logout() {
        // 這裡可以實現登出邏輯
        this.$router.push('/login');
      },
    },
  };
  </script>
  
  <style scoped>
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
    top: 10px; /* 調整此值以增加與標題的距離 */
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
    left: -250px; /* Initially hide the sidebar */
    height: 100%;
    transition: left 0.3s ease;
}

.sidebar.active {
    left: 0; /* Show the sidebar */
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
    background-color: #333; /* Match sidebar background color */
    border-radius: 0; /* Remove border-radius */
    display: block; /* Ensure links take up full width */
    transition: background-color 0.3s;
    box-sizing: border-box;
}

.sidebar a:hover {
    background-color: #444; /* Darken on hover */
}

.main-content {
    flex: 1;
    padding: 60px 20px 20px 20px; /* 調整 padding-top 以與 .hamburger-menu 保持距離 */
    margin-left: 0; /* Initial position without sidebar */
    transition: margin-left 0.3s ease;
}

.main-content.shifted {
    margin-left: 250px; /* Shift when sidebar is visible */
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

iframe {
    width: 100%;
    height: calc(100vh - 40px); /* 高度根據視窗大小調整 */
    border: none;
}

  </style>
  