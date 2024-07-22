<!-- src/App.vue -->
<template>
    <div id="app">
      <Sidebar @toggleSidebar="toggleSidebar"/>
      <MainContent :isSidebarCollapsed="isSidebarCollapsed"/>
    </div>
  </template>
  
  <script>
  import Sidebar from '@/components/Sidebar.vue';
  import MainContent from '@/components/MainContent.vue';
  
  export default {
    components: {
      Sidebar,
      MainContent
    },
    data() {
      return {
        isSidebarCollapsed: false
      };
    },
    methods: {
      toggleSidebar() {
        this.isSidebarCollapsed = !this.isSidebarCollapsed;
      }
    }
  };
  </script>
  
  <style>
  /* 包含你在原始 HTML 中的 CSS */
  </style>
  