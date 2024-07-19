<template>
    <div>
 
  
  
      <form class="change-password-form" @submit.prevent="handleSubmit">
        <div class="input-container">
          <label for="currentPassword">原密碼：</label>
          <input type="password" id="currentPassword" v-model="currentPassword">
        </div>
        <div class="input-container">
          <label for="newPassword">新密碼：</label>
          <input type="password" id="newPassword" v-model="newPassword">
        </div>
        <div class="input-container">
          <label for="confirmNewPassword">新密碼確認：</label>
          <input type="password" id="confirmNewPassword" v-model="confirmNewPassword">
        </div>
  
        <div class="button-container">
          <button type="submit">更改</button>
          <button type="button" class="cancel" @click="cancelChanges">取消變更</button>
        </div>
      </form>
  
      <div class="back-home">
        <button @click="goHome">返回首頁</button>
      </div>
  
      <div class="navbar">
        <div class="dropdown">

          
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ChangePassword',
    data() {
      return {
        currentPassword: '',
        newPassword: '',
        confirmNewPassword: ''
      };
    },
    methods: {
      handleSubmit() {
        // 處理密碼變更邏輯
        console.log('密碼變更提交', this.currentPassword, this.newPassword, this.confirmNewPassword);
        alert('密碼已更改');
      },
      cancelChanges() {
        alert('您取消了變更密碼');
      },
      goHome() {
        this.$router.push('/home');
      },
      logout() {
        alert('已登出');
        this.$router.push('/login');
      }
    }
  };
  </script>
  
  <style scoped src="../assets/css/ChangePassword.css"></style>
  