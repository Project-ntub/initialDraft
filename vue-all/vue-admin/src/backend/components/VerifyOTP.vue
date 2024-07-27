<template>
    <div class="container">
      <h1>OTP 驗證</h1>
      <form @submit.prevent="verifyOtp">
        <div class="form-group">
          <label for="otp">OTP:</label>
          <input type="text" v-model="otp" id="otp" required />
        </div>
        <button type="submit" class="btn">驗證</button>
        <p v-if="error" class="error">{{ error }}</p>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "VerifyOtp",
    data() {
      return {
        otp: "",
        error: null
      };
    },
    methods: {
      verifyOtp() {
        // 發送請求到後端
        this.$http.post("/backend/verify_otp", { otp: this.otp })
          .then(response => {
            if (response.data.success) {
              this.$router.push({ name: 'home' });
            } else {
              this.error = "驗證失敗";
            }
          });
      }
    }
  };
  </script>
  
  <style scoped src="../assets/css/VerifyOTP.css"></style>

  