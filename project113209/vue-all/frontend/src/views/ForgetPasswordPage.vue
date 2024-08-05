<template>
  <div class="container">
    <h2>忘記密碼</h2>
    <form @submit.prevent="sendPasswordReset">
      <label for="email">電子郵件：</label>
      <input type="email" id="email" v-model="email" required>
      <button type="submit">發送</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: 'ForgetPasswordPage',
  data() {
    return {
      email: ''
    };
  },
  methods: {
    sendPasswordReset() {
      if (this.email) {
        axios.post('/frontend/forgot_password/', { email: this.email })
          .then(() => {
            alert('已發送密碼重設請求至您的電子郵件');
          })
          .catch(error => {
            console.error('Error sending password reset request:', error);
            alert('發送失敗，請重試');
          });
      } else {
        alert('請輸入有效的電子郵件地址');
      }
    }
  }
};
</script>

<style scoped src="../assets/css/ForgetPasswordPage.css"></style>
