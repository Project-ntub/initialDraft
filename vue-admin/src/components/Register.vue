<template>
    <div class="container">
      <h2>註冊</h2>
      <form @submit.prevent="register">
        <div v-if="error" class="error">
          <p>{{ error }}</p>
        </div>
        <label for="username">用戶名:</label>
        <input type="text" id="username" v-model="form.username" required />
  
        <label for="email">電子郵件:</label>
        <input type="email" id="email" v-model="form.email" required />
        <button type="button" @click="getVerificationCode">獲取驗證碼</button>
        <div id="verification-feedback" class="feedback">{{ feedback }}</div>
  
        <label for="verification_code">驗證碼:</label>
        <input type="text" id="verification_code" v-model="form.verification_code" required />
        <button type="button" @click="validateVerificationCode">驗證碼驗證</button>
        <div id="verification-feedback" class="feedback">{{ feedback }}</div>
  
        <label for="password">密碼:</label>
        <input type="password" id="password" v-model="form.password" required />
  
        <label for="confirm_password">確認密碼:</label>
        <input type="password" id="confirm_password" v-model="form.confirm_password" required />
  
        <label for="phone">手機號碼:</label>
        <input type="text" id="phone" v-model="form.phone" required />
  
        <input type="submit" value="註冊" />
  
        <p class="terms">
          點擊「註冊」表示您同意我們的 <a href="#">服務條款</a> 和
          <a href="#">隱私政策</a>
        </p>
      </form>
    </div>
  </template>
  
  <script>
  import axios from '../axios';
  
  export default {
    name: 'AppRegister',
    data() {
      return {
        form: {
          username: '',
          email: '',
          verification_code: '',
          password: '',
          confirm_password: '',
          phone: '',
        },
        error: '',
        feedback: '',
      };
    },
    methods: {
      getVerificationCode() {
        const email = this.form.email.trim();
        if (!this.validateEmail(email)) {
          alert('請輸入有效的電子郵件地址。');
          return;
        }
  
        axios
          .get(`/backend/send_verification_code/?email=${encodeURIComponent(email)}`)
          .then((response) => {
            if (response.data.success) {
              alert('驗證碼已發送到您的電子郵件。');
              this.feedback = '驗證碼已發送到您的電子郵件，有效期限5分鐘。';
            } else {
              alert('發送驗證碼失敗。');
              this.feedback = '發送驗證碼失敗，請重試。';
            }
          })
          .catch(() => {
            alert('發送驗證碼失敗。');
            this.feedback = '發送驗證碼失敗，請重試。';
          });
      },
      validateVerificationCode() {
        const email = this.form.email.trim();
        const verificationCode = this.form.verification_code.trim();
        if (verificationCode === '') {
          alert('請輸入驗證碼。');
          return;
        }
  
        axios
          .get(`/backend/verify_code/?email=${encodeURIComponent(email)}&code=${encodeURIComponent(verificationCode)}`)
          .then((response) => {
            if (response.data.success) {
              alert('驗證碼有效。');
              this.feedback = '驗證碼有效。';
            } else {
              alert('驗證碼無效或已過期。');
              this.feedback = '驗證碼無效或已過期，請重試。';
            }
          })
          .catch(() => {
            alert('驗證碼驗證失敗。');
            this.feedback = '驗證碼驗證失敗，請重試。';
          });
      },
      validateEmail(email) {
        const re = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
        return re.test(String(email).toLowerCase());
      },
      register() {
        // 在此處處理註冊邏輯，例如調用 API 以完成註冊
        // 使用 this.form 中的數據發送請求
        console.log('Registering user:', this.form);
        // 額外的註冊邏輯可以在這裡實現
      },
    },
  };
  </script>
  
  <style scoped>
  body {
    font-family: Arial, sans-serif;
    background-color: #f2f2f2;
    margin: 0;
    padding: 0;
  }
  
  .container {
    max-width: 400px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    text-align: center;
    margin-bottom: 30px;
  }
  
  label {
    font-weight: bold;
    display: block;
    margin-bottom: 5px;
  }
  
  input[type="text"],
  input[type="email"],
  input[type="password"],
  input[type="submit"],
  button {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
    border: 1px solid #ccc;
    box-sizing: border-box;
  }
  
  button {
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  input[type="submit"] {
    background-color: #28a745;
    color: #fff;
    border: none;
    cursor: pointer;
  }
  
  input[type="submit"]:hover {
    background-color: #218838;
  }
  
  .terms {
    font-size: 12px;
    text-align: center;
  }
  
  .terms a {
    color: #007bff;
    text-decoration: none;
  }
  
  .error {
    color: red;
    margin-top: -15px;
    margin-bottom: 20px;
    text-align: center;
  }
  </style>
  