<template>
  <div>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      :data-target="target"
      :aria-controls="target"
      :aria-expanded="toggled"
      aria-label="Toggle navigation"
      @click="toggleMenu"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div v-if="showMenu" class="dropdown-menu">
      <div @click="goToPreferences">偏好設定</div>
      <div @click="logout">登出</div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    target: {
      type: String,
      required: true,
      description: "Button target element ID",
    },
    toggled: {
      type: Boolean,
      default: false,
      description: "Whether button is toggled",
    },
  },
  data() {
    return {
      showMenu: false,
    };
  },
  methods: {
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
    goToPreferences() {
      this.$router.push('/userpreferences');
    },
    logout() {
      console.log('Logout clicked');
      this.$router.push('/logout');
    },
  },
};
</script>

<style>
/* Add your styles here */
</style>
