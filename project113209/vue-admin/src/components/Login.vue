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

<style scoped src="../assets/css/login.css"></style>