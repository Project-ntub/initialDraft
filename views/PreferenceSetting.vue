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
          <div class="header">偏好設定</div>
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
  methods: {
    toggleMenu() {
      const dropdownContent = document.querySelector('.dropdown-content');
      dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
    },
    cancelChanges() {
      this.fontSize = 'medium';
      this.notification = 'disable';
      this.autoLogin = 'disable';
      this.authentication = 'disable';
    },
    submitChanges() {
      const fontSize = this.fontSize === 'large' ? '18px' : this.fontSize === 'small' ? '12px' : '16px';
      document.body.style.fontSize = fontSize;
      alert('偏好設定已更改');
    }
  },
};
</script>

<style scoped src="../assets/css/PreferenceSetting.css"></style>
