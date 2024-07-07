<template>
  <div id="app">
    <navbar v-if="!isNoSidebarLayout" />
    <sidebar v-if="!isNoSidebarLayout" />
    <router-view />
  </div>
</template>

<script>
export default {
  computed: {
    isNoSidebarLayout() {
      return this.$route.meta.layout === 'no-sidebar';
    }
  }
};
</script>
