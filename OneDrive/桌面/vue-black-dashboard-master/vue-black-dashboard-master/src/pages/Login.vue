<template>
  <div class="login-container">
    <div class="login-box">
      <h2>Login</h2>
      <form @submit.prevent="login">
        <div class="input-group">
          <label for="username">帳號</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="input-group">
          <label for="password">密碼</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="input-group remember-me">
          <input type="checkbox" id="rememberMe" v-model="rememberMe">
          <label for="rememberMe">記住我</label>
        </div>
        <button type="submit" class="btn btn-primary">登入</button>
        <router-link to="/forgot-password" class="forgot-password">忘記密碼?</router-link>
        <router-link to="/register" class="btn btn-secondary">註冊</router-link>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      rememberMe: false,
    };
  },
  mounted() {
    // 页面加载时，检查是否已经在登录页面，如果不是，则跳转到登录页面
    if (this.$route.path !== '/login') {
      this.$router.push({ name: 'Login' });
    }
  },
  methods: {
    login() {
      // 處理登入邏輯，例如向伺服器發送登入請求
      console.log('Logging in:', {
        username: this.username,
        password: this.password,
        rememberMe: this.rememberMe,
      });
      // 在此添加你的登入邏輯，例如API調用
      // 如果登入成功，則導航到主頁
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.login-box {
  width: 400px;
  padding: 20px;
  background-color: white;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
}

.input-group input[type="text"],
.input-group input[type="password"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.remember-me {
  display: flex;
  align-items: center;
}

.remember-me input {
  margin-right: 10px;
}

button.btn {
  width: 100%;
  padding: 10px;
  margin-top: 10px;
}

.forgot-password {
  display: block;
  text-align: center;
  margin-top: 10px;
}

button.btn-secondary {
  margin-top: 10px;
  width: 100%;
}
</style>
