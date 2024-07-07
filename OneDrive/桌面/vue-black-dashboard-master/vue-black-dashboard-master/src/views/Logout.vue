<template>
  <div class="logout-page">
    <div class="container">
      <h1 class="text-center">登出成功</h1>
      <p class="text-center">感謝您的使用！</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Logout",
  mounted() {
    // 清除用户的登录状态
    localStorage.removeItem('isAuthenticated');

    // 使用 $nextTick 确保导航在 DOM 更新完成后进行
    this.$nextTick(() => {
      this.$router.replace('/login');
    });
  }
};
</script>

<style scoped>
.logout-page {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #ffffff; /* 白色背景 */
}

.container {
  text-align: center;
}

.btn-center {
  display: inline-block;
  margin-top: 20px;
}
</style>
