<template>
  <div class="login-container">
    <div class="login-box">
      <h2>註冊</h2>
      <form @submit.prevent="register">
        <div class="input-group">
          <label for="username">帳號/用戶名:</label>
          <input type="text" id="username" v-model="username" required>
        </div>

        <div class="input-group">
          <label for="email">電子郵件:</label>
          <input type="email" id="email" v-model="email" required>
          <button type="button" @click="sendVerificationCode">發送驗證碼</button>
        </div>

        <div v-if="codeSent" class="input-group">
          <label for="verification_code">驗證碼:</label>
          <input type="text" id="verification_code" v-model="verification_code" required>
        </div>

        <div class="input-group">
          <label for="password">密碼:</label>
          <input type="password" id="password" v-model="password" required>
        </div>

        <div class="input-group">
          <label for="confirm_password">再次輸入密碼:</label>
          <input type="password" id="confirm_password" v-model="confirm_password" required>
        </div>

        <div class="input-group">
          <label for="phone">行動電話:</label>
          <input type="tel" id="phone" v-model="phone" required>
        </div>

        <div class="button-group">
          <button type="submit" class="btn btn-primary">註冊</button>
          <button type="button" @click="goToLogin" class="btn btn-secondary">返回登入</button>
        </div>

        <p class="terms">點擊「註冊」表示您同意我們的 <a href="#">服務條款</a> 和 <a href="#">隱私政策</a></p>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirm_password: '',
      phone: '',
      verification_code: '',
      codeSent: false // 新增狀態表示是否已發送驗證碼
    };
  },
  methods: {
    sendVerificationCode() {
      // 發送驗證碼的邏輯
      console.log('Sending verification code to:', this.email);

      // 使用 Axios 發送 API 請求
      axios.post('/api/send-verification', { email: this.email })
        .then(response => {
          console.log('Verification code sent:', response.data);
          this.codeSent = true; // 標記已發送驗證碼
        })
        .catch(error => {
          console.error('Error sending verification code:', error);
        });
    },
    register() {
      // 處理註冊邏輯
      console.log('Registering:', {
        username: this.username,
        email: this.email,
        password: this.password,
        confirm_password: this.confirm_password,
        phone: this.phone,
        verification_code: this.verification_code
      });

      // 在此處添加你的註冊邏輯，例如API調用
      axios.post('/api/register', {
        username: this.username,
        email: this.email,
        password: this.password,
        confirm_password: this.confirm_password,
        phone: this.phone,
        verification_code: this.verification_code
      })
      .then(response => {
        console.log('Registration successful:', response.data);
        this.$router.push('/login');
      })
      .catch(error => {
        console.error('Registration failed:', error);
      });
    },
    goToLogin() {
      // 點擊返回按鈕時執行的方法
      this.$router.push('/login');
    }
  }
};
</script>

<style src="@/assets/css/RegisterPage.css"></style>
