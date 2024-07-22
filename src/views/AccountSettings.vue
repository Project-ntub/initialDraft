<template>
  <div class="account-settings-page">
    <!-- Sidebar component -->
    <SidebarPage />
    <div class="main-panel">
      <div class="container">
        <div class="account-settings">
          <!-- 用户头像 -->
          <img class="profile-pic" src="https://via.placeholder.com/100" alt="Profile Picture">
          <!-- 用户名 -->
          <h3>wang</h3>
          <!-- 修改密码链接 -->
          <router-link to="/changepassword" class="setting-option">
            <img src="https://img.icons8.com/ios-filled/50/000000/lock.png" alt="修改密碼">
            修改密碼
          </router-link>
          <!-- 偏好设置链接 -->
          <router-link to="/preferences" class="setting-option">
            <img src="https://img.icons8.com/ios-filled/50/000000/settings.png" alt="偏好設定">
            偏好設定
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SidebarPage from '@/components/SidebarPage.vue';

export default {
  name: 'AccountSettings',
  components: {
    SidebarPage, // 导入侧边栏组件
  },
};
</script>

<style scoped>
/* body {
  font-family: Arial, sans-serif;
  padding: 0;
  margin: 0;
  background-color: #f2f2f2;
} */

/* 调整 account-settings 的样式 */
.account-settings {
  /* background-color: white; 
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  */
  padding: 20px; 
  width: 80%; 
  max-width: 400px;
  margin: 50px auto; 
  text-align: center; 
}

/* 用户头像样式 */
.account-settings img.profile-pic {
  border-radius: 50%; /* 圆形头像 */
  width: 100px; /* 宽度 */
  height: 100px; /* 高度 */
  margin-bottom: 20px; /* 底部外边距 */
}

/* 用户名样式 */
.account-settings h3 {
  margin-top: 0; /* 顶部外边距 */
  font-size: 24px; /* 字体大小 */
  color: #333; /* 颜色 */
}

/* 设置选项的样式 */
.account-settings .setting-option {
  display: flex; /* 使用 flex 布局 */
  align-items: center; /* 垂直居中 */
  justify-content: center; /* 水平居中 */
  margin: 10px 0; /* 上下外边距 */
  font-size: 18px; /* 字体大小 */
  color: #333; /* 颜色 */
  text-decoration: none; /* 去掉下划线 */
}

/* 设置选项图标的样式 */
.account-settings .setting-option img {
  width: 24px; /* 宽度 */
  height: 24px; /* 高度 */
  margin-right: 10px; /* 右外边距 */
}
</style>
