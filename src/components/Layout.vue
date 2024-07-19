<!-- src/components/Layout.vue -->
<!-- eslint-disable vue/multi-word-component-names -->
<template>
    <div :class="['layout', { 'sidebar-expanded': isSidebarExpanded }]">
      <SidebarPage @toggleSidebar="handleSidebarToggle" />
      <div class="main-panel">
        <TopNavbar /> <!-- 顶部导航栏 -->
        <router-view /> <!-- 路由视图，将在这里加载页面内容 -->
      </div>
    </div>
  </template>
  
  <script>
  import SidebarPage from './SidebarPage.vue'; // 导入侧边栏组件
  import TopNavbar from './TopNavbar.vue'; // 导入顶部导航栏组件
  
  export default {
    name: 'AppLayout', // 更改组件名称以符合 ESLint 规则
    components: {
      SidebarPage,
      TopNavbar,
    },
    data() {
      return {
        isSidebarExpanded: false, // 控制侧边栏展开或收起状态
      };
    },
    methods: {
      handleSidebarToggle(isExpanded) {
        this.isSidebarExpanded = isExpanded; // 更新侧边栏状态
      },
    },
  };
  </script>
  
  <style scoped>
  .layout {
    display: flex; /* 使用flex布局 */
  }
  
  .sidebar-expanded .main-panel {
    margin-left: 200px; /* 侧边栏展开时主面板的左边距 */
  }
  
  .main-panel {
    flex-grow: 1; /* 主面板占满剩余空间 */
    padding: 20px;
    margin-left: 60px; /* 侧边栏收起时主面板的左边距 */
  }
  </style>
  