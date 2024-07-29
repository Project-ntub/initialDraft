<template>
    <div>
      <div class="header-bar">重設密碼</div>
      <div class="container">
        <h2>重設密碼</h2>
        <form>
          <label for="newPassword">新密碼：</label>
          <div class="input-container">
            <input type="password" id="newPassword" v-model="newPassword">
            <i class="fas fa-eye toggle-password" @click="togglePasswordVisibility('newPassword')"></i>
          </div>
  
          <label for="confirmPassword">確認密碼：</label>
          <div class="input-container">
            <input type="password" id="confirmPassword" v-model="confirmPassword">
            <i class="fas fa-eye toggle-password" @click="togglePasswordVisibility('confirmPassword')"></i>
          </div>
  
          <button type="button" @click="resetPassword">重設密碼</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ResetPasswordPage',
    data() {
      return {
        newPassword: '',
        confirmPassword: ''
      };
    },
    methods: {
      resetPassword() {
        const urlParams = new URLSearchParams(window.location.search);
        const email = urlParams.get('email');
        const token = urlParams.get('token');
  
        if (this.newPassword !== this.confirmPassword) {
          alert('密碼不匹配');
          return;
        }
  
        fetch('http://localhost:3001/resetpassword', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email: email, token: token, newPassword: this.newPassword })
        })
          .then(response => response.json())
          .then(data => {
            alert(data.message);
            if (data.success) {
              this.$router.push('/reset-success');
            }
          })
          .catch(error => console.error('Error:', error));
      },
      togglePasswordVisibility(id) {
        const passwordInput = document.getElementById(id);
        const eyeIcon = passwordInput.nextElementSibling;
        if (passwordInput.type === 'password') {
          passwordInput.type = 'text';
          eyeIcon.classList.remove('fa-eye');
          eyeIcon.classList.add('fa-eye-slash');
        } else {
          passwordInput.type = 'password';
          eyeIcon.classList.remove('fa-eye-slash');
          eyeIcon.classList.add('fa-eye');
        }
      }
    }
  };
  </script>
  
  <style scoped>
  @import "../assets/css/ResetPasswordPage.css";
  </style>
  