<template>
  <div class="reset-password-container">
    <h2>重置密碼</h2>
    <form @submit.prevent="handleSubmit">
      <label for="password">新密碼：</label>
      <input type="password" id="password" v-model="password" required />
      <label for="confirmPassword">確認新密碼：</label>
      <input type="password" id="confirmPassword" v-model="confirmPassword" required />
      <button type="submit">提交</button>
    </form>
    <div v-if="message">{{ message }}</div>
  </div>
</template>

<script>
import axios from 'axios';
import '@/assets/css/ResetPasswordPage.css'; 

export default {
  data() {
    return {
      password: '',
      confirmPassword: '',
      message: '',
      token: ''
    };
  },
  created() {
    this.token = this.$route.params.token;
  },
  methods: {
    handleSubmit() {
      if (this.password !== this.confirmPassword) {
        this.message = '兩次密碼輸入不一致。';
        return;
      }
      axios.post(`http://localhost:8000/frontend/reset_password/${this.token}/`, {
        password: this.password
      })
        .then(() => {
          this.message = '密碼重置成功！';
        })
        .catch(error => {
          console.error('Error resetting password:', error);
          this.message = '重置失敗，請重試。';
        });
    }
  }
};
</script>
