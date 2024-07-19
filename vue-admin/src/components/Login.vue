<template>
  <div class="container">
    <h2>登入</h2>
    <form @submit.prevent="login">
      <input type="hidden" name="next" value="/management" />
      <div class="form-group">
        <label for="email">帳號:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="password">密碼:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div class="form-group">
        <input type="checkbox" id="remember_me" v-model="rememberMe" />
        <label for="remember_me">記住我</label>
      </div>
      <button type="submit" class="btn-login">登入</button>
    </form>
    <p>
      還未擁有帳號? <router-link to="/register">註冊</router-link>
    </p>
    <p>
      忘記密碼? <router-link to="/forgot_password">重置密碼</router-link>
    </p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from '../axios'; // 使用配置好的 axios 实例
// import '../assets/login.css'; // 確保文件名大小寫正確

export default {
  name: 'AppLogin',
  data() {
    return {
      email: '',
      password: '',
      rememberMe: false,
      error: ''
    };
  },
  
  methods: {
        async login() {
      try {
        const csrfToken = getCookie('csrftoken');
        const response = await axios.post('/api/token/', {
          email: this.email,
          password: this.password,
          remember_me: this.rememberMe
        }, {
          headers: {
            'X-CSRFToken': csrfToken
          }
        });
        console.log('登入成功', response);
        localStorage.setItem('token', response.data.access); // 確保令牌被存儲
        this.$router.push('/management');
      } catch (error) {
        console.error('登入失败', error.response);
        if (error.response && error.response.data) {
          this.error = error.response.data.detail || '登入失敗，請檢查您的使用者名稱和密碼';
        } else {
          this.error = '登入失敗，請稍後再試';
        }
      }
    }
  }
};

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
</script>

<style scoped>
body {
  font-family: Arial, sans-serif !important;
  background-color: #f4f4f4 !important;
  margin: 0 !important;
  padding: 0 !important;
  display: flex !important;
  justify-content: center !important;
  align-items: flex-start !important;
  min-height: 100vh !important;
}

.container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
}
.form-group {
  margin-bottom: 20px;
}
.form-group label {
  display: block;
  font-weight: bold;
  margin-bottom: 5px;
}
.form-group input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}
.form-group input[type="checkbox"] {
  width: auto;
  display: inline;
}
.btn-login {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}
.btn-login:hover {
  background-color: #0056b3;
}

</style>