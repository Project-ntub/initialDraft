<template>
    <div>
      
      <div class="content" id="content">
        <div class="container">
          <h2>忘記密碼</h2>
          <form @submit.prevent="sendPasswordReset">
            <label for="email">電子郵件：</label>
            <input type="email" id="email" v-model="email" required>
            <button type="submit">發送</button>
          </form>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ForgetPasswordPage',
    data() {
      return {
        email: ''
      };
    },
    methods: {
      toggleSidebar() {
        const sidebar = document.getElementById('sidebar');
        const content = document.getElementById('content');
        sidebar.classList.toggle('open');
        content.classList.toggle('shift');
      },
      sendPasswordReset() {
        const email = this.email.trim();
        
        fetch('http://localhost:3001/forgot-password', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email })
        })
        .then(response => {
          if (!response.ok) {
            return response.json().then(error => { throw new Error(error.message); });
          }
          return response.json();
        })
        .then(data => alert(data.message))
        .catch(error => alert('Error: ' + error.message));
      }
    }
  };
  </script>
  
  <style scoped>
  @import '../assets/css/ForgetPasswordPage.css';
  </style>
  