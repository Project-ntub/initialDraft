<template>
  <div class="login-container">
    <div class="login-form">
      <h2>登入</h2>
      <form @submit.prevent="login">
        <div class="input-group">
          <label for="username">帳號</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="input-group">
          <label for="password">密碼</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div class="remember-me">
          <input type="checkbox" id="remember-me" v-model="rememberMe" />
          <label for="remember-me">記住我</label>
        </div>
        <button type="submit" class="login-button">登入</button>
        <div class="links">
          <router-link to="/register">註冊</router-link>
          <router-link to="/forgetpassword">忘記密碼?</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      rememberMe: false,
    };
  },
  methods: {
    login() {
      console.log('Logging in...', this.username, this.password, this.rememberMe);
      this.$router.push({ name: '首頁' });
    },
  },
};
</script>

<style scoped src="../assets/css/LoginPage.css"></style>
