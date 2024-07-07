<template>
  <div class="login-container">
    <div class="login-box">
      <h2>User Registration</h2>
      <form @submit.prevent="register">
        <div class="input-group">
          <label for="username">帳號/用戶名:</label>
          <input type="text" id="username" v-model="username" required>
        </div>

        <div class="input-group">
          <label for="email">電子郵件:</label>
          <input type="email" id="email" v-model="email" required>
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

        <div class="input-group">
          <label for="verification_code">驗證碼:</label>
          <input type="text" id="verification_code" v-model="verification_code" required>
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
export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirm_password: '',
      phone: '',
      verification_code: ''
    };
  },
  methods: {
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
      // 如果註冊成功，則導航到登入頁面
      this.$router.push('/login');
    },
    goToLogin() {
      // 點擊返回按鈕時執行的方法
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  width: 100vw; /* 設置寬度為100%視窗寬度 */
  background-color: #f5f5f5; /* 背景顏色改為灰色 */
}

.login-box {
  width: 400px;
  padding: 20px;
  background-color: #ffffff; /* 背景顏色改為白色 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  margin-top: 20px;
}

.input-group {
  margin-bottom: 15px;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
  font-size: 14px; /* 字體大小統一 */
}

.input-group input[type="text"],
.input-group input[type="email"],
.input-group input[type="password"],
.input-group input[type="tel"],
.input-group input[type="submit"],
.input-group input[type="button"] {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px; /* 字體大小統一 */
}

.button-group {
  display: flex;
  justify-content: space-between;
}

button.btn {
  flex: 1;
  padding: 10px;
  margin-top: 10px;
  color: #fff;
  border: none;
  cursor: pointer;
  font-size: 14px;
}

button.btn.btn-primary {
  background-color: #007bff; /* 註冊按鈕顏色改為藍色 */
}

button.btn.btn-secondary {
  background-color: #6c757d; /* 返回按鈕顏色稍微區別 */
}

button.btn:hover {
  opacity: 0.9;
}

.terms {
  font-size: 12px;
  text-align: center;
}

.terms a {
  color: #007bff;
  text-decoration: none;
}

.back-link {
  display: block;
  text-align: center;
  margin-top: 10px;
  font-size: 14px;
  color: #007bff;
  text-decoration: none;
}

.back-link:hover {
  text-decoration: underline;
}
</style>
