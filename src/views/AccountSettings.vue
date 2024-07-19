/* eslint-disable vue/multi-word-component-names */
<template>
  <div>
    <div class="container">
      <div class="account-settings">
        <img class="profile-pic" src="https://via.placeholder.com/100" alt="Profile Picture">
        <h3>wang</h3>
        <router-link to="/changepassword" class="setting-option">
          <img src="https://img.icons8.com/ios-filled/50/000000/lock.png" alt="修改密碼">
          修改密碼
        </router-link>
        <router-link to="/preferences" class="setting-option">
          <img src="https://img.icons8.com/ios-filled/50/000000/settings.png" alt="偏好設定">
          偏好設定
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AccountSettingsPage', // 更改组件名称为多字
};
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  padding: 0;
  margin: 0;
  background-color: #f2f2f2;
}
.container {
  margin-top: 80px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
  width: 90%;
  max-width: 600px;
  margin: 0 auto;
}
.account-settings {
  background-color: white;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  width: 100%;
  text-align: center;
}
.account-settings img.profile-pic {
  border-radius: 50%;
  width: 100px;
  height: 100px;
  margin-bottom: 20px;
}
.account-settings h3 {
  margin-top: 0;
  font-size: 24px;
  color: #333;
}
.account-settings .setting-option {
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 10px 0;
  font-size: 18px;
  color: #333;
  text-decoration: none;
}
.account-settings .setting-option img {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}
</style>
