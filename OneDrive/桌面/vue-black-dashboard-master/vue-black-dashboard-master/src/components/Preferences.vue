<template>
    <div class="preferences-dialog">
      <h3 style="font-size: 1.5em; font-weight: bold;">偏好設置</h3>
  
      <div class="preference-item">
        <label for="fontSize" style="margin-right: 10px;">字體大小：</label>
        <select v-model="fontSize" @change="updateFontSize">
          <option value="medium">適中</option>
          <option value="large">大</option>
        </select>
      </div>
  
      <div class="preference-item">
        <label for="autoLogin" style="margin-right: 10px;">自動登錄：</label>
        <select v-model="autoLogin" @change="updateAutoLogin">
          <option :value="false">取消自動登入</option>
          <option :value="true">開啟自動登入</option>
        </select>
      </div>
  
      <div class="preference-item">
        <label for="notifications" style="margin-right: 10px;">通知：</label>
        <select v-model="notifications" @change="updateNotifications">
          <option :value="true">開啟通知</option>
          <option :value="false">關閉通知</option>
        </select>
      </div>
  
      <div class="button-group">
        <button class="save-button" @click="savePreferences">保存</button>
        <button class="cancel-button" @click="cancelPreferences">取消</button>
      </div>
  
      <div v-if="message" class="message">{{ message }}</div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        fontSize: 'medium',
        autoLogin: false,
        notifications: true,
        rootFontSize: '16px', // 初始根元素字體大小
        originalPreferences: {}, // 用於存儲初始偏好設置
        message: '' // 用於顯示保存成功的訊息
      };
    },
    methods: {
      updateFontSize() {
        switch (this.fontSize) {
          case 'medium':
            this.rootFontSize = '16px';
            break;
          case 'large':
            this.rootFontSize = '24px';
            break;
          default:
            this.rootFontSize = '16px'; // 預設為適中大小
            break;
        }
        this.updateRootFontSize(); // 更新根元素字體大小
      },
      updateRootFontSize() {
        document.documentElement.style.fontSize = this.rootFontSize;
      },
      updateAutoLogin() {
        // Logic for auto-login
      },
      updateNotifications() {
        // Logic for notifications
      },
      savePreferences() {
        // Save preferences to local storage or backend
        localStorage.setItem('preferences', JSON.stringify({
          fontSize: this.fontSize,
          autoLogin: this.autoLogin,
          notifications: this.notifications,
        }));
        this.message = '保存成功！';
        setTimeout(() => this.message = '', 3000); // 3秒後清除訊息
        this.$emit('close');
      },
      cancelPreferences() {
        // 恢復到原始偏好設置
        this.fontSize = this.originalPreferences.fontSize;
        this.autoLogin = this.originalPreferences.autoLogin;
        this.notifications = this.originalPreferences.notifications;
        this.updateFontSize();
        this.$emit('close');
      }
    },
    mounted() {
      const preferences = localStorage.getItem('preferences');
      const savedPreferences = preferences ? JSON.parse(preferences) : null;
  
      if (savedPreferences) {
        this.fontSize = savedPreferences.fontSize;
        this.autoLogin = savedPreferences.autoLogin;
        this.notifications = savedPreferences.notifications;
        this.updateFontSize(); // 初始化時更新字體大小
      }
  
      // 保存初始偏好設置
      this.originalPreferences = {
        fontSize: this.fontSize,
        autoLogin: this.autoLogin,
        notifications: this.notifications
      };
    }
  };
  </script>
  
  <style scoped>
  .preferences-dialog {
    max-width: 300px;
    margin: 0;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
  }
  
  .preference-item {
    margin-bottom: 10px;
  }
  
  .button-group {
    display: flex;
    justify-content: space-between;
  }
  
  .save-button, .cancel-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .cancel-button {
    background-color: #dc3545;
  }
  
  .save-button:hover {
    background-color: #0056b3;
  }
  
  .cancel-button:hover {
    background-color: #c82333;
  }
  
  .message {
    margin-top: 10px;
    color: green;
    font-weight: bold;
  }
  </style>
  