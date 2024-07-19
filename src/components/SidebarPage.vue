<template>
  <div :class="['sidebar', { open: isOpen }]"> <!-- 侧边栏的容器，动态添加 'open' 类 -->
    <div class="logo-details"> <!-- 包含Logo和用户名的区域 -->
      <i class='fas fa-user icon'></i> <!-- 用户图标 -->
      <div class="logo_name">{{ userName }}</div> <!-- 显示用户名 -->
      <i class='bx bx-menu' id="btn" @click="toggleSidebar"></i> <!-- 切换侧边栏状态的按钮 -->
    </div>
    <ul class="nav-list"> <!-- 导航链接列表 -->
      <li v-for="(link, index) in sidebarLinks" :key="index"> <!-- 循环渲染每个链接 -->
        <router-link :to="link.path" class="nav-link" @click="closeSidebarIfOpen"> <!-- 导航链接 -->
          <i :class="link.icon"></i> <!-- 链接图标 -->
          <span class="links_name">{{ link.name }}</span> <!-- 链接名称 -->
        </router-link>
        <span class="tooltip">{{ link.name }}</span> <!-- 链接的工具提示 -->
      </li>
      <li class="profile"> <!-- 登出按钮 -->
        <i class='fas fa-sign-out-alt' id="log_out" @click="logout"></i> <!-- 登出图标，点击触发登出方法 -->
        <span class="tooltip">登出</span> <!-- 工具提示：登出 -->
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'SidebarPage', // 组件名
  data() {
    return {
      sidebarLinks: [ // 侧边栏链接数据
        { path: '/home', name: '首頁', icon: 'fas fa-home' }, // 首页链接
        { path: '/accountsettings', name: '帳號設定', icon: 'fas fa-cog' }, // 账号设置链接
        { path: '/profile', name: '個人資訊', icon: 'fas fa-user' }, // 个人信息链接
        { path: '/history', name: '歷史紀錄', icon: 'fas fa-history' }, // 历史记录链接
      ],
      userName: '王大明', // 用户名
      isOpen: false // 侧边栏初始状态
    };
  },
  methods: {
  toggleSidebar() { // 切换侧边栏状态的方法
  this.isOpen = !this.isOpen; // 切换状态
  document.querySelector('.sidebar').classList.toggle('open'); // 切换 'open' 类
  if (this.isOpen) {
    document.body.classList.add('open-sidebar'); // 添加 body 的 'open-sidebar' 类
  } else {
    document.body.classList.remove('open-sidebar'); // 移除 body 的 'open-sidebar' 类
  }
  this.$emit('toggleSidebar', this.isOpen); // 触发自定义事件
},
closeSidebarIfOpen() { // 如果侧边栏是打开状态则关闭它
  if (this.isOpen) { // 检查侧边栏是否打开
    this.isOpen = false;
    document.querySelector('.sidebar').classList.remove('open'); // 移除 'open' 类
    document.body.classList.remove('open-sidebar'); // 移除 body 的 'open-sidebar' 类
    this.$emit('toggleSidebar', this.isOpen); // 触发自定义事件
  }
},

    logout() { // 登出方法
      console.log('Logging out...'); // 打印日志信息
      this.$router.push({ name: 'Login' }); // 重定向到登录页面
    }
  }
};
</script>

<style scoped src="../assets/css/SidebarPage.css"></style> <!-- 引入外部CSS文件 -->
