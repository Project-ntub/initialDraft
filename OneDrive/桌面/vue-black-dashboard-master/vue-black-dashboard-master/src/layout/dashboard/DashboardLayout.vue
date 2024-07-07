<template>
  <!-- 定義 Vue 單文件組件的模板部分開始 -->
  <div class="wrapper">
    <!-- 包裹整個應用的主要容器 -->
    <side-bar>
      <!-- 包含側邊欄組件 -->
      <template slot="links">
        <!-- 側邊欄連結模板，用來定義側邊欄中的各個連結項目 -->
        <sidebar-link
          to="/dashboard"
          :name="$t('首頁')"
          icon="tim-icons icon-chart-pie-36"
        />
        <sidebar-link
          to="/accountsettings"
          :name="$t('帳號設定')"
          icon="tim-icons icon-bell-55"
        />
        <sidebar-link
          to="/profile"
          :name="$t('個人資訊')"
          icon="tim-icons icon-single-02"
        />
        <sidebar-link
          to="/historyrecord"
          :name="$t('歷史紀錄')"
          icon="tim-icons icon-puzzle-10"
        />

      </template>
    </side-bar>
    <div class="main-panel">
      <!-- 主要面板部分 -->
      <top-navbar></top-navbar>
      <!-- 頁面的頂部導航欄組件 -->

      <dashboard-content @click.native="toggleSidebar"> </dashboard-content>
      <!-- 控制側邊欄顯示/隱藏的內容區域 -->

      <content-footer></content-footer>
      <!-- 頁面的底部內容組件 -->
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./TopNavbar.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
export default {
  components: {
    TopNavbar,
    DashboardContent,
  },
  methods: {
    toggleSidebar() {
      // 定義一個方法來切換側邊欄的顯示狀態
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);
      }
    },
  },
};
</script>
