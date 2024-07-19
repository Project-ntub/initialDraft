<template>
    <div class="forgot-password">
      <h2>忘記密碼</h2>
      <form>
        <label for="username">帳戶：</label>
        <input type="text" id="username" v-model="username">
  
        <label for="email">電子郵件：</label>
        <input type="email" id="email" v-model="email">
  
        <button type="button" @click="sendPasswordReset" class="btn btn-primary">發送</button>
        <button type="button" @click="goBack" class="btn btn-secondary">返回</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ForgetPasswordPage',
    data() {
      return {
        username: '',
        email: ''
      };
    },
    methods: {
      sendPasswordReset() {
        alert('已發送密碼重置郵件到 ' + this.email);
      },
      goBack() {
        this.$router.go(-1); // 返回上一頁
      }
    }
  }
  </script>
  
  <style scoped>
  .forgot-password {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh; /* 使區塊高度為整個視窗高度 */
    padding: 20px;
    background-color: #ffffff; /* 設置整個區塊的背景色為白色 */
  }
  
  h2 {
    font-size: 24px; /* 設置標題字體大小 */
    margin-bottom: 20px; /* 調整標題與表單之間的距離 */
  }
  
  form {
    width: 100%;
    max-width: 400px; /* 調整表單的最大寬度 */
    padding: 20px;
    background-color: #f9f9f9; /* 設置表單區塊背景色 */
    border: 1px solid #ccc;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 添加陰影效果 */
  }
  
  label {
    display: block;
    font-size: 16px; /* 調整標籤字體大小 */
    margin-bottom: 10px; /* 調整標籤下方的間距 */
  }
  
  input[type="text"],
  input[type="email"],
  button {
    width: 100%;
    padding: 10px; /* 調整輸入框和按鈕的內邊距 */
    margin-bottom: 20px; /* 調整輸入框和按鈕之間的距離 */
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
    font-size: 16px; /* 調整輸入框和按鈕字體大小 */
  }
  
  button.btn-primary {
    background-color: #007bff; /* 與登入按鈕相同的背景顏色 */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button.btn-primary:hover {
    background-color: #0056b3; /* 懸停時的背景顏色 */
  }
  
  button.btn-secondary {
    background-color: #6c757d; /* 與登入頁面的註冊按鈕相同的背景顏色 */
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button.btn-secondary:hover {
    background-color: #5a6268; /* 懸停時的背景顏色 */
  }
  </style>
  