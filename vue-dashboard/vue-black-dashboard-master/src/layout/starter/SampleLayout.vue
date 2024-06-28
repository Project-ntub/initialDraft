<template>
  <div class="wrapper">
    <!-- 左側側邊欄 -->
    <side-bar>
      <template slot="links">
        <!-- 側邊欄連結至儀表板 -->
        <!-- :name="$t('sidebar.dashboard')"  // 使用翻譯函數顯示儀表板連結名稱 -->
        <!-- icon="tim-icons icon-chart-pie-36"使用圖標顯示儀表板連結 -->
        <sidebar-link
          to="/dashboard"
          :name="$t('sidebar.dashboard')"
          icon="tim-icons icon-chart-pie-36"
        />
      </template>
    </side-bar>
    <!-- 主面板 -->
    <div class="main-panel">
       <!-- 頂部導航欄 -->
      <top-navbar></top-navbar>

      <dashboard-content @click.native="toggleSidebar"> </dashboard-content>
      <!-- 儀表板內容 -->
      <!-- <content-footer></content-footer> -->
    </div>
  </div>
</template>
<style lang="scss"></style>
<script>
import TopNavbar from "./SampleNavbar.vue";  // 引入頂部導航欄組件
// import ContentFooter from "./SampleFooter.vue";  // 引入內容頁腳組件
import DashboardContent from "./Content.vue";  // 引入儀表板內容組件
export default {
  components: {
    TopNavbar,
    // ContentFooter,
    DashboardContent,
  },
  methods: {
    // 方法：切換側邊欄的顯示狀態
    toggleSidebar() {
      if (this.$sidebar.showSidebar) {
        this.$sidebar.displaySidebar(false);  // 如果側邊欄顯示中，則隱藏側邊欄
      }
    },
  },
};
</script>
