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
          :name="$t('sidebar.dashboard')"
          icon="tim-icons icon-chart-pie-36"
        />
        <!-- 第一個側邊欄連結 -->
        <!-- <sidebar-link
          to="/icons"
          :name="$t('sidebar.icons')"
          icon="tim-icons icon-atom"
        /> -->
        <!-- 第二個側邊欄連結 -->
        <!-- <sidebar-link
          to="/maps"
          :name="$t('sidebar.maps')"
          icon="tim-icons icon-pin"
        /> -->
        <!-- 第三個側邊欄連結 -->
        <sidebar-link
          to="/notifications"
          :name="$t('sidebar.notifications')"
          icon="tim-icons icon-bell-55"
        />
        <!-- 第四個側邊欄連結 -->
        <sidebar-link
          to="/profile"
          :name="$t('sidebar.userProfile')"
          icon="tim-icons icon-single-02"
        />
        <!-- 第五個側邊欄連結 -->
        <!-- <sidebar-link
          to="/table-list"
          :name="$t('sidebar.tableList')"
          icon="tim-icons icon-puzzle-10"
        /> -->
        <!-- 第六個側邊欄連結 -->
        <!-- <sidebar-link
          to="/typography"
          :name="$t('sidebar.typography')"
          icon="tim-icons icon-align-center"
        /> -->
        <!-- 第七個側邊欄連結 -->
        <!-- <sidebar-link
          to="/dashboard?enableRTL=true"
          :name="$t('sidebar.rtlSupport')"
          icon="tim-icons icon-world"
        /> -->
        <!-- 第八個側邊欄連結 -->
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
import ContentFooter from "./ContentFooter.vue";
import DashboardContent from "./Content.vue";
import MobileMenu from "./MobileMenu";
export default {
  components: {
    TopNavbar,
    ContentFooter,
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
