<template>
    <div>
      <h2>忘記密碼</h2>
      <form @submit.prevent="forgotPassword">
        <div class="form-group">
          <label for="username">帳戶：</label>
          <input type="text" v-model="username" id="username" required />
        </div>
        <div class="form-group">
          <label for="email">電子郵件：</label>
          <input type="email" v-model="email" id="email" required />
        </div>
        <button type="submit">發送</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "ForgotPassword",
    data() {
      return {
        username: "",
        email: ""
      };
    },
    methods: {
      forgotPassword() {
        // 發送請求到後端
        this.$http.post("/forgot_password", { username: this.username, email: this.email })
          .then(response => {
            if (response.data.success) {
              alert("密碼重置請求已發送");
            } else {
              alert("請求失敗");
            }
          });
      }
    }
  };
  </script>
  
  <style scoped src="../assets/css/ForgotPassword.css"></style>

  