<template>
  <!-- Navbar component -->
  <nav
    class="navbar navbar-expand-lg navbar-absolute"
    :class="{ 'bg-white': showMenu, 'navbar-transparent': !showMenu }"
  >
    <div class="container-fluid">
      <!-- Navbar wrapper -->
      <div class="navbar-wrapper">
        <!-- Navbar toggle button -->
        <div
          class="navbar-toggle d-inline"
          :class="{ toggled: $sidebar.showSidebar }"
        >
          <button
            type="button"
            class="navbar-toggler"
            aria-label="Navbar toggle button"
            @click="toggleSidebar"
          >
            <span class="navbar-toggler-bar bar1"></span>
            <span class="navbar-toggler-bar bar2"></span>
            <span class="navbar-toggler-bar bar3"></span>
          </button>
        </div>
        <!-- Navbar brand -->
        <a class="navbar-brand" href="#pablo">{{ routeName }}</a>
      </div>
      <!-- Mobile menu toggle button -->
      <button
        class="navbar-toggler"
        type="button"
        @click="toggleMenu"
        data-toggle="collapse"
        data-target="#navigation"
        aria-controls="navigation-index"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-bar navbar-kebab"></span>
        <span class="navbar-toggler-bar navbar-kebab"></span>
        <span class="navbar-toggler-bar navbar-kebab"></span>
      </button>

      <!-- Collapsible menu content -->
      <collapse-transition>
        <div class="collapse navbar-collapse show" v-show="showMenu">
          <ul class="navbar-nav" :class="$rtl.isRTL ? 'mr-auto' : 'ml-auto'">
            <!-- Notifications dropdown -->
            <base-dropdown
              tag="li"
              :menu-on-right="!$rtl.isRTL"
              title-tag="a"
              class="nav-item"
            >
              <a
                slot="title"
                href="#"
                class="dropdown-toggle nav-link"
                data-toggle="dropdown"
                aria-expanded="true"
              >
                <div class="notification d-none d-lg-block d-xl-block"></div>
                <i class="tim-icons icon-sound-wave"></i>
                <p class="d-lg-none">New Notifications</p>
              </a>
              <li class="nav-link">
                <a href="#" class="nav-item dropdown-item"
                  >Mike John responded to your email</a
                >
              </li>
              <li class="nav-link">
                <a href="#" class="nav-item dropdown-item"
                  >You have 5 more tasks</a
                >
              </li>
              <li class="nav-link">
                <a href="#" class="nav-item dropdown-item"
                  >Your friend Michael is in town</a
                >
              </li>
              <li class="nav-link">
                <a href="#" class="nav-item dropdown-item"
                  >Another notification</a
                >
              </li>
              <li class="nav-link">
                <a href="#" class="nav-item dropdown-item">Another one</a>
              </li>
            </base-dropdown>

            <!-- User profile dropdown -->
            <base-dropdown
              tag="li"
              :menu-on-right="!$rtl.isRTL"
              title-tag="a"
              class="nav-item"
              menu-classes="dropdown-navbar"
            >
              <a
                slot="title"
                href="#"
                class="dropdown-toggle nav-link"
                data-toggle="dropdown"
                aria-expanded="true"
              >
                <div class="photo">
                  <img src="img/anime3.png" />
                </div>
                <b class="caret d-none d-lg-block d-xl-block"></b>
              </a>
              <li class="nav-link">
                <router-link class="nav-item dropdown-item" to="/userpreferences">偏好設定</router-link>
              </li>
              <div class="dropdown-divider"></div>
              <li class="nav-link">
                <router-link class="nav-item dropdown-item" to="/logout">登出</router-link>
              </li>
            </base-dropdown>
          </ul>
        </div>
      </collapse-transition>
    </div>
  </nav>
</template>

<script>
import { CollapseTransition } from "vue2-transitions";
import Modal from "@/components/Modal";

export default {
  components: {
    CollapseTransition,
    Modal,
  },
  computed: {
    routeName() {
      const { name } = this.$route;
      return this.capitalizeFirstLetter(name);
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
  },
  data() {
    return {
      activeNotifications: false,
      showMenu: false,
      searchModalVisible: false,
      searchQuery: "",
    };
  },
  methods: {
    capitalizeFirstLetter(string) {
      return string.charAt(0).toUpperCase() + string.slice(1);
    },
    toggleNotificationDropDown() {
      this.activeNotifications = !this.activeNotifications;
    },
    closeDropDown() {
      this.activeNotifications = false;
    },
    toggleSidebar() {
      this.$sidebar.displaySidebar(!this.$sidebar.showSidebar);
    },
    hideSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    toggleMenu() {
      this.showMenu = !this.showMenu;
    },
  },
};
</script>

<style></style>
