<template>
  <div id="app">
    <SidebarPage v-if="!$route.meta.hideSidebar" />
    <router-view />
  </div>
</template>

<script>
import SidebarPage from './components/SidebarPage.vue';

export default {
  name: 'App',
  components: {
    SidebarPage,
  },
};
</script>

<style>
@import '~@fortawesome/fontawesome-free/css/all.css';

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
