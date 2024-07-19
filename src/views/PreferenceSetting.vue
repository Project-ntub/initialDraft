<template>
  <div class="preferences-page">
    <div class="preferences-dialog">
      <h3 class="title">偏好設置</h3>
      <div class="preference-item">
        <label for="fontSize">字體大小：</label>
        <select id="fontSize" v-model="fontSize" @change="updateFontSize">
          <option value="medium">適中</option>
          <option value="large">大</option>
        </select>
      </div>
      <div class="preference-item">
        <label for="autoLogin">自動登錄：</label>
        <select id="autoLogin" v-model="autoLogin" @change="updateAutoLogin">
          <option :value="false">取消自動登入</option>
          <option :value="true">開啟自動登入</option>
        </select>
      </div>
      <div class="preference-item">
        <label for="notifications">通知：</label>
        <select id="notifications" v-model="notifications" @change="updateNotifications">
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
  </div>
</template>

<script>
export default {
  name: 'PreferenceSetting',
  data() {
    return {
      fontSize: 'medium',
      autoLogin: false,
      notifications: true,
      rootFontSize: '16px',
      originalPreferences: {},
      message: ''
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
          this.rootFontSize = '16px';
          break;
      }
      this.updateRootFontSize();
    },
    updateRootFontSize() {
      document.documentElement.style.fontSize = this.rootFontSize;
    },
    updateAutoLogin() {},
    updateNotifications() {},
    savePreferences() {
      localStorage.setItem('preferences', JSON.stringify({
        fontSize: this.fontSize,
        autoLogin: this.autoLogin,
        notifications: this.notifications,
      }));
      this.message = '保存成功！';
      setTimeout(() => this.message = '', 3000);
      this.$emit('close');
    },
    cancelPreferences() {
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
      this.updateFontSize();
    }
    this.originalPreferences = {
      fontSize: this.fontSize,
      autoLogin: this.autoLogin,
      notifications: this.notifications
    };
  }
};
</script>

<style scoped>
.preferences-page {
  display: flex;
  align-items: flex-start;
  padding: 20px;
}

.preferences-dialog {
  width: 300px;
  margin-top: 20px;
  margin-left: 250px; /* 调整左边距 */
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #f9f9f9;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
}

.title {
  font-size: 1.5em;
  font-weight: bold;
  text-align: center;
}

.preference-item {
  margin-bottom: 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.preference-item label {
  flex: 1;
  text-align: left;
  margin-right: 10px;
}

.preference-item select {
  flex: 2;
  padding: 5px;
  font-size: 1.1em;
}

.button-group {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.save-button, .cancel-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  flex: 1;
  margin: 0 5px;
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
  text-align: center;
}
</style>
