<template>
  <div id="app">
    <TopNavbar v-if="showTopNavbar" />
    <SidebarPage v-if="!$route.meta.hideSidebar" />
    <router-view />
  </div>
</template>

<script>
import TopNavbar from './components/TopNavbar.vue';
import SidebarPage from './components/SidebarPage.vue';

export default {
  name: 'App',
  components: {
    TopNavbar,
    SidebarPage
  },
  computed: {
    showTopNavbar() {
      return !this.$route.meta.hideNavbar;
    }
  }
};
</script>

<style>
/* 你的样式 */
</style>
