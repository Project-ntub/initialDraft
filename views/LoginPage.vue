<template>
  <div class="login-container">
    <div class="login-form">
      <h2>用戶登入</h2>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="email">電子郵件</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="input-group">
          <label for="password">密碼</label>
          <div class="input-container">
            <input type="password" id="password" v-model="password" required />
            <i class="fas fa-eye toggle-password" @click="togglePasswordVisibility('password')"></i>
          </div>
        </div>
        <div class="additional-options">
          <label>
            <input type="checkbox" id="rememberMe" v-model="rememberMe" />
            記住我
          </label>
          <router-link to="/forgetpassword">忘記密碼?</router-link>
        </div>
        <input type="submit" value="登入" class="submit-button" />
        <div id="login-feedback" class="feedback">{{ loginFeedback }}</div>
      </form>
      <p>還未擁有帳號？ <router-link to="/register">註冊</router-link></p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      rememberMe: false,
      loginFeedback: ''
    };
  },
  methods: {
    handleLogin() {
      // 模擬登錄成功的邏輯，無論輸入什麼都認為登錄成功
      this.loginFeedback = '登入成功';
      this.$router.push('/home'); // 成功登錄後重定向到首頁
    },
    togglePasswordVisibility(inputId) {
      const passwordInput = document.getElementById(inputId);
      if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
      } else {
        passwordInput.type = 'password';
      }
    }
  }
};
</script>

<style scoped src="@/assets/css/LoginPage.css"></style>
