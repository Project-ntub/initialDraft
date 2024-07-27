<!-- src/components/MainContent.vue -->
<template>
    <div :class="['main-content', { 'collapsed': isSidebarCollapsed }]">
      <button class="toggle-btn" @click="toggleSidebar">≡</button>
      <router-view></router-view>
    </div>
  </template>
  
  <script>
  export default {
    props: ['isSidebarCollapsed'],
    methods: {
      toggleSidebar() {
        this.$emit('toggleSidebar');
      }
    }
  };
  </script>
  
  <style scoped>
  /* 包含你在原始 HTML 中的 CSS */
  </style>

