<template>
  <div class="message">
    <h1>註冊成功</h1>
    <p>您已成功註冊。感謝您的使用。</p>
    <button @click="goToLogin">返回登入頁面</button>
  </div>
</template>

<script>
export default {
  name: "RegistrationSuccess",
  methods: {
    goToLogin() {
      this.$router.push({ name: 'login' });
    }
  }
};
</script>

<style scoped src="../assets/css/RegistrationSuccess.css"></style>
