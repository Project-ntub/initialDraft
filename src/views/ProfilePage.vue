<template>
    <div class="profile-page">
      <!-- 个人卡片 -->
      <div class="profile-card-container">
        <PersonalCard :userData="userData" @edit="toggleEdit" />
      </div>
      <!-- 编辑个人资料表单 -->
      <div v-if="showEdit" class="edit-profile-container">
        <form @submit.prevent="saveProfile">
          <div class="input-group-container">
            <div class="input-group">
              <label for="edit-account">帳號</label>
              <input type="text" id="edit-account" v-model="localData.account" disabled>
            </div>
            <div class="input-group">
              <label for="edit-email">電子郵件</label>
              <input type="email" id="edit-email" v-model="localData.email">
            </div>
            <div class="input-group">
              <label for="edit-name">姓名</label>
              <input type="text" id="edit-name" v-model="localData.name">
            </div>
          </div>
          <div class="input-group-container">
            <div class="input-group">
              <label for="edit-department">部門</label>
              <input type="text" id="edit-department" v-model="localData.department" disabled>
            </div>
            <div class="input-group">
              <label for="edit-position">職位</label>
              <input type="text" id="edit-position" v-model="localData.position" disabled>
            </div>
            <div class="input-group">
              <label for="edit-phone">電話</label>
              <input type="text" id="edit-phone" v-model="localData.phone">
            </div>
          </div>
          <div class="button-container">
            <button type="submit" class="save-button">儲存</button>
            <button type="button" class="cancel-button" @click="cancelEdit">取消</button>
          </div>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import PersonalCard from './PersonalCard.vue';
  import '@/assets/css/ProfilePage.css'; // 引入新的 CSS 文件
  
  export default {
    name: 'ProfilePage',
    components: {
      PersonalCard
    },
    data() {
      return {
        userData: {
          avatar: '', // 这里可以填充实际的默认值
          name: 'John Doe',
          account: 'johndoe123',
          department: '行銷部',
          position: '經理',
          phone: '123-456-7890',
          email: 'johndoe@example.com'
        },
        showEdit: false,
        localData: {}
      };
    },
    methods: {
      toggleEdit() {
        this.localData = { ...this.userData };
        this.showEdit = !this.showEdit;
      },
      saveProfile() {
        this.userData = { ...this.localData };
        this.showEdit = false;
      },
      cancelEdit() {
        this.localData = { ...this.userData };
        this.showEdit = false;
      }
    }
  };
  </script>
  
  <style scoped>
  /* 如果有其他特定于这个组件的样式，可以在这里添加 */
  </style>
  