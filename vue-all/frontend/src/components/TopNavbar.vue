<template>
 <nav class="navbar">
    <div class="navbar-title">{{ currentRouteName }}</div>
    <div v-if="isHomePage" class="export-container">
      <button class="export-button" @click="toggleExportMenu">匯出</button>
      <div v-if="showExportMenu" class="export-menu">
        <button @click="exportFile('pdf')">匯出PDF</button>
        <button @click="exportFile('excel')">匯出Excel</button>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      showExportMenu: false
    };
  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    },
    isHomePage() {
      return this.$route.name === '首頁'; // 确认首页的路由名称
    }
  },
  methods: {
    toggleExportMenu() {
      this.showExportMenu = !this.showExportMenu;
    },
    exportFile(type) {
      this.$emit('export', type);
      this.showExportMenu = false;
    }
  }
};
</script>


<style scoped>
.navbar {
  background-color: #333;
  color: #fff;
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: center; /* 修改为两端对齐 */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 1000;
}

.navbar-title {
  font-size: 30px;
  font-weight: bold;
}

.export-container {
  position: absolute;
  right: 70px; /* 右边距离 */
}

.export-button {
  background-color: #6200ea;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  margin-top: 20px; /* 增加上边距 */
  margin-right: 20px;
  font-size: 16px;
  font-weight: bold;
}

.export-button:hover {
  background-color: #3700b3;

}

.export-menu {
  position: absolute;
  top: 69px;
  right: 0;
  background-color: #fff;
  border: 1px solid #ddd;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}

.export-menu button {
  background-color: #fff;
  color: #333;
  border: none;
  padding: 5px 35px;
  width: 100%;
  /* text-align: left; */
  cursor: pointer;
  font-size: 15px;
}

.export-menu button:hover {
  background-color: #f1f1f1;
}
</style>
