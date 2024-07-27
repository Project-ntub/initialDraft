<template>
  <div class="content" id="content">
    <div class="container">
      <h2>註冊</h2>
      <form @submit.prevent="handleSubmit">
        <label for="username">用戶名</label>
        <input type="text" id="username" v-model="username" required />

        <label for="email">電子郵件</label>
        <input type="email" id="email" v-model="email" required />

        <button type="button" @click="getVerificationCode">獲取驗證碼</button>
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

        <input type="submit" value="註冊" class="submit-button"/>
      </form>
    </div>
  </div>
</template>

<script>
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
      this.verificationFeedback = '驗證碼已發送到您的電子郵件，有效期限5分鐘。';
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

      alert('註冊成功！');
    },
  },
};
</script>

<style scoped>
.submit-button {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  margin-top: 10px;
}

.submit-button:hover {
  background-color: #0056b3;
}

.password-container {
  position: relative;
}

.toggle-password {
  position: absolute;
  right: 10px;
  top: 50%;
  transform: translateY(-50%);
  cursor: pointer;
}

.password-example {
  font-size: 12px;
  color: #666;
}

.feedback {
  color: red;
  font-size: 14px;
  margin-top: 10px;
}
</style>
