<template>
    <div class="profile-container">
      <h2>個人資料</h2>
      <label for="name">姓名：</label>
      <input type="text" id="name" v-model="profile.name">
      
      <label for="username">帳號：</label>
      <input type="text" id="username" v-model="profile.username">
      
      <label for="department">部門：</label>
      <input type="text" id="department" v-model="profile.department">
      
      <label for="position">職位：</label>
      <input type="text" id="position" v-model="profile.position">
      
      <label for="phone">電話：</label>
      <input type="text" id="phone" v-model="profile.phone">
      
      <label for="email">電子郵件：</label>
      <input type="text" id="email" v-model="profile.email">
      
      <label for="created">建立時間：</label>
      <input type="text" id="created" v-model="profile.created" disabled>
  
      <button @click="openModal">編輯</button>
      <button class="logout-btn" @click="logout">登出</button>
    </div>
  
    <div id="editModal" class="modal" v-if="showModal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>編輯個人資料</h2>
        <label for="modal-name">姓名：</label>
        <input type="text" id="modal-name" v-model="editProfile.name">
        
        <label for="modal-username">帳號：</label>
        <input type="text" id="modal-username" v-model="editProfile.username">
        
        <label for="modal-department">部門：</label>
        <input type="text" id="modal-department" v-model="editProfile.department">
        
        <label for="modal-position">職位：</label>
        <input type="text" id="modal-position" v-model="editProfile.position">
        
        <label for="modal-phone">電話：</label>
        <input type="text" id="modal-phone" v-model="editProfile.phone">
        
        <label for="modal-email">電子郵件：</label>
        <input type="text" id="modal-email" v-model="editProfile.email">
  
        <button @click="saveProfile">保存</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        profile: {
          name: 'John Doe',
          username: 'johndoe123',
          department: '技術部',
          position: '系統管理員',
          phone: '0912345678',
          email: 'johndoe@example.com',
          created: '2023-01-01'
        },
        editProfile: {
          name: 'John Doe',
          username: 'johndoe123',
          department: '技術部',
          position: '系統管理員',
          phone: '0912345678',
          email: 'johndoe@example.com'
        },
        showModal: false
      };
    },
    methods: {
      openModal() {
        this.editProfile = { ...this.profile };
        this.showModal = true;
      },
      closeModal() {
        this.showModal = false;
      },
      saveProfile() {
        this.profile = { ...this.editProfile };
        this.closeModal();
        alert('個人資料已更新');
      },
      logout() {
        window.location.href = '登出成功.html';
      }
    }
  };
  </script>
  
  <style scoped>
  /* 在此處添加你的 CSS */
  body {
      font-family: Arial, sans-serif;
      padding: 20px;
      background-color: #f4f4f4;
  }
  .profile-container {
      max-width: 600px;
      margin: 0 auto;
      background-color: #fff;
      padding: 20px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
  }
  .profile-container h2 {
      margin-bottom: 20px;
      font-size: 24px;
  }
  .profile-container p {
      margin: 10px 0;
      font-size: 18px;
  }
  .profile-container label {
      display: block;
      margin: 5px 0;
  }
  .profile-container input {
      width: 100%;
      padding: 8px;
      margin: 5px 0 20px;
      border: 1px solid #ccc;
      border-radius: 4px;
  }
  .profile-container button {
      padding: 10px 20px;
      margin-right: 10px;
      background-color: #3498db;
      color: #fff;
      border: none;
      border-radius: 4px;
      cursor: pointer;
  }
  .profile-container button:hover {
      background-color: #2980b9;
  }
  .profile-container .logout-btn {
      background-color: #e74c3c;
  }
  .profile-container .logout-btn:hover {
      background-color: #c0392b;
  }
  .modal {
      display: none;
      position: fixed;
      z-index: 1;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      overflow: auto;
      background-color: rgba(0, 0, 0, 0.4);
  }
  .modal-content {
      background-color: #fff;
      margin: 15% auto;
      padding: 20px;
      border: 1px solid #888;
      width: 80%;
      max-width: 400px;
      border-radius: 8px;
  }
  .close {
      color: #aaa;
      float: right;
      font-size: 28px;
      font-weight: bold;
  }
  .close:hover,
  .close:focus {
      color: black;
      text-decoration: none;
      cursor: pointer;
  }
  </style>
  