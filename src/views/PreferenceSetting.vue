<template>
    <div>
      <div class="header-bar">偏好設定</div>
      <button class="hamburger-menu" @click="toggleMenu">
        <div></div>
        <div></div>
        <div></div>
      </button>
  
      <SidebarPage />
  
      <div class="content" id="content">
        <div class="container">
          <div class="preferences">
            <div class="header">
              偏好設定
            </div>
            <div class="form-group">
              <label for="font-size">字體大小</label>
              <select id="font-size" v-model="fontSize">
                <option value="large">大</option>
                <option value="medium">適中</option>
                <option value="small">小</option>
              </select>
            </div>
            <div class="form-group">
              <label for="notification">通知設定</label>
              <select id="notification" v-model="notification">
                <option value="enable">開啟通知</option>
                <option value="disable">關閉通知</option>
              </select>
            </div>
            <div class="form-group">
              <label for="auto-login">自動登入</label>
              <select id="auto-login" v-model="autoLogin">
                <option value="enable">自動登入</option>
                <option value="disable">取消自動登入</option>
              </select>
            </div>
            <div class="form-group">
              <label for="authentication">認證設定</label>
              <select id="authentication" v-model="authentication">
                <option value="enable">開啟認證</option>
                <option value="disable">關閉認證</option>
              </select>
            </div>
            <div class="buttons">
              <button class="cancel-button" @click="cancelChanges">取消變更</button>
              <button class="submit-button" @click="submitChanges">更改</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import SidebarPage from '@/components/SidebarPage.vue';
  
  export default {
    name: 'PreferenceSetting',
    components: {
      SidebarPage,
    },
    data() {
      return {
        fontSize: 'medium',
        notification: 'disable',
        autoLogin: 'disable',
        authentication: 'disable',
      };
    },
    mounted() {
      // 從資料庫中獲取上次的偏好設定
      fetch('/api/user-data')
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            const user = data.data[0];
            this.fontSize = user.font_size;
            this.notification = user.notifications_enabled ? 'enable' : 'disable';
            this.autoLogin = user.auto_login_enabled ? 'enable' : 'disable';
            this.authentication = user.authentication_enabled ? 'enable' : 'disable';
  
            const fontSize = this.fontSize === 'large' ? '18px' : this.fontSize === 'small' ? '12px' : '16px';
            document.body.style.fontSize = fontSize;
          }
        })
        .catch(error => {
          console.error('獲取偏好設定錯誤:', error);
        });
  
      const storedFontSize = localStorage.getItem('fontSize');
      if (storedFontSize) {
        document.body.style.fontSize = storedFontSize;
      }
    },
    methods: {
      toggleMenu() {
        const dropdownContent = document.querySelector('.dropdown-content');
        if (dropdownContent.style.display === 'block') {
          dropdownContent.style.display = 'none';
        } else {
          dropdownContent.style.display = 'block';
        }
      },
      cancelChanges() {
        // 還原表單值為當前的偏好設定
        this.$data = this.$options.data();
        this.mounted();
      },
      submitChanges() {
        const fontSize = this.fontSize;
        const notification = this.notification;
        const autoLogin = this.autoLogin;
        const authentication = this.authentication;
  
        fetch('/update-preferences', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ fontSize, notification, autoLogin, authentication })
        })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            alert('偏好設定更新成功');
          } else {
            alert('偏好設定更新失敗，請重試。');
          }
        })
        .catch(error => {
          console.error('偏好設定更新錯誤:', error);
          alert('偏好設定更新失敗，請重試。');
        });
      }
    },
  };
  </script>
  
  <style scoped src="../assets/css/PreferenceSetting.css"></style>
  