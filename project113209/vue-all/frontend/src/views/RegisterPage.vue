<template>
  <div class="content" id="content">
    <div class="container">
      <h2>註冊</h2>
      <form @submit.prevent="handleSubmit">
        <label for="username">用戶名</label>
        <input type="text" id="username" v-model="username" required />

        <label for="email">電子郵件</label>
        <input type="email" id="email" v-model="email" required />

        <button type="button" class="verification-button" @click="getVerificationCode">獲取驗證碼</button>
        <div id="verification-feedback" class="feedback">{{ verificationFeedback }}</div>

        <label for="verification_code">驗證碼</label>
        <input type="text" id="verification_code" v-model="verificationCode" required />

        <label for="password">密碼</label>
        <div class="password-container">
          <input type="password" id="password" v-model="password" required />
          <span class="toggle-password" @click="handleTogglePassword">👁️</span>
        </div>
        <div class="password-example">密碼必須包含至少8個字符，且包括大小寫字母、數字和特殊字符。例如：Password@123</div>

        <label for="confirm_password">確認密碼</label>
        <div class="password-container">
          <input type="password" id="confirm_password" v-model="confirmPassword" required />
          <span class="toggle-password" @click="handleTogglePassword">👁️</span>
        </div>

        <label for="phone">電話號碼</label>
        <input type="text" id="phone" v-model="phone" required />

        <div class="button-container">
          <input type="submit" value="註冊" class="submit-button" />
          <button type="button" class="back-button" @click="goBack">返回上一頁</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirmPassword: '',
      phone: '',
      verificationCode: '',
      verificationFeedback: '',
    };
  },
  methods: {
    getVerificationCode() {
      if (!this.validateEmail(this.email)) {
        alert('請輸入有效的電子郵件地址。');
        return;
      }

      axios.get(`/frontend/send_verification_code/?email=${this.email}`)
        .then(() => {
          this.verificationFeedback = '驗證碼已發送到您的電子郵件，有效期限5分鐘。';
        })
        .catch(error => {
          console.error('Error sending verification code:', error);
          this.verificationFeedback = '發送驗證碼失敗，請重試。';
        });
    },
    validateEmail(email) {
      const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
      return re.test(String(email).toLowerCase());
    },
    validatePassword(password) {
      const re = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
      return re.test(password);
    },
    handleTogglePassword(event) {
      const passwordInput = event.target.previousElementSibling;
      if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
        event.target.innerText = '👁️';
      } else {
        passwordInput.type = 'password';
        event.target.innerText = '👁️';
      }
    },
    handleSubmit() {
      if (this.password !== this.confirmPassword) {
        alert('密碼與確認密碼不匹配。');
        return;
      }

      if (!this.validatePassword(this.password)) {
        alert('密碼必須包含至少8個字符，且包括大小寫字母、數字和特殊字符。例如：Password@123');
        return;
      }

      const userData = {
        username: this.username,
        email: this.email,
        password: this.password,
        confirmPassword: this.confirmPassword,
        phone: this.phone,
        verificationCode: this.verificationCode
      };

      console.log(userData);  // 打印請求數據，確認 email 欄位不為空

      axios.post('/frontend/register/', userData)
        .then(() => {
          alert('註冊成功！');
          this.$router.push('/login'); // 跳转到登录页面
        })
        .catch(error => {
          console.error('Error registering user:', error);
          alert('註冊失敗，請重試。');
        });
    },
    goBack() {
      this.$router.go(-1); // 返回上一頁
    }
  },
};
</script>

<style scoped src="../assets/css/RegisterPage.css"></style>
