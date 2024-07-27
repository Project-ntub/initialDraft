<template>
    <div>
    
      <div class="content" id="content">
        <div class="container">
          <h2>註冊</h2>
          <form @submit.prevent="handleSubmit">
            <label for="username">用戶名</label>
            <input type="text" id="username" v-model="username" required>
  
            <label for="email">電子郵件</label>
            <input type="email" id="email" v-model="email" required>
  
            <!-- <button type="button" @click="getVerificationCode">獲取驗證碼</button>
            <div id="verification-feedback" class="feedback">{{ verificationFeedback }}</div> -->
  
            <!-- <label for="verification_code">驗證碼</label>
            <input type="text" id="verification_code" v-model="verificationCode" required> -->
  
            <label for="password">密碼</label>
            <div class="password-container">
              <input type="password" id="password" v-model="password" required>
              <span class="toggle-password" @click="togglePassword('password')">👁️</span>
            </div>
            <div class="password-example">密碼必須包含至少8個字符，且包括大小寫字母、數字和特殊字符。例如：Password@123</div>
  
            <label for="confirm_password">確認密碼</label>
            <div class="password-container">
              <input type="password" id="confirm_password" v-model="confirmPassword" required>
              <span class="toggle-password" @click="togglePassword('confirm_password')">👁️</span>
            </div>
  
            <label for="phone">電話號碼</label>
            <input type="text" id="phone" v-model="phone" required>
  
            <input type="submit" value="註冊">
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'RegisterPage',
    data() {
      return {
        username: '',
        email: '',
        password: '',
        confirmPassword: '',
        phone: '',
        verificationCode: '',
        verificationFeedback: ''
      };
    },
    methods: {
      toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        const content = document.getElementById('content');
        sidebar.classList.toggle('open');
        content.classList.toggle('shift');
      },
      getVerificationCode() {
        const email = this.email.trim();
        if (!this.validateEmail(email)) {
          alert('請輸入有效的電子郵件地址。');
          return;
        }
  
        fetch('/send-verification', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email })
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            alert('驗證碼已發送到您的電子郵件。');
            this.verificationFeedback = '驗證碼已發送到您的電子郵件，有效期限5分鐘。';
          } else {
            alert('發送驗證碼失敗，請重試。');
          }
        })
        .catch(error => {
          console.error('Error:', error);
          alert('發送驗證碼失敗，請重試。');
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
      togglePassword(field) {
        const passwordField = document.getElementById(field);
        passwordField.type = passwordField.type === 'password' ? 'text' : 'password';
      },
      handleSubmit() {
        const username = this.username.trim();
        const email = this.email.trim();
        const password = this.password.trim();
        const confirmPassword = this.confirmPassword.trim();
        const phone = this.phone.trim();
        const inputCode = this.verificationCode.trim();
  
        if (password !== confirmPassword) {
          alert('密碼與確認密碼不匹配。');
          return;
        }
  
        if (!this.validatePassword(password)) {
          alert('密碼必須包含至少8個字符，且包括大小寫字母、數字和特殊字符。例如：Password@123');
          return;
        }
  
        fetch('/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ username, email, password, phone, inputCode })
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            this.$router.push('/login'); // 成功後重定向到登入頁面
          } else {
            alert(data.message);
          }
        })
        .catch(error => {
          console.error('Error:', error);
          alert('註冊失敗，請重試。');
        });
      }
    }
  };
  </script>
  
  <style scoped>
  @import '../assets/css/RegisterPage.css';
  </style>
  