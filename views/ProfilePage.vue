<template>
  <div>
    <div class="content" :class="{ shift: isSidebarOpen }" id="content">
      <div class="info-container">
        <h3>個人資訊</h3>
        <div v-if="!isEditing">
          <p>姓名：<span>{{ userData.username }}</span></p>
          <p>帳號：<span>{{ userData.username }}</span></p>
          <p>部門：<span>{{ userData.department_id }}</span></p>
          <p>職位：<span>{{ userData.position_id }}</span></p>
          <p>電話：<span>{{ userData.phone }}</span></p>
          <p>電子郵件：<span>{{ userData.email }}</span></p>
          <div class="button-container">
            <button class="edit" @click="editProfile">編輯</button>
          </div>
        </div>
        <div v-else>
          <p>姓名：<input type="text" v-model="editData.username"></p>
          <p>帳號：<input type="text" v-model="editData.username"></p>
          <p>部門：<input type="text" v-model="editData.department_id"></p>
          <p>職位：<input type="text" v-model="editData.position_id"></p>
          <p>電話：<input type="text" v-model="editData.phone"></p>
          <p>電子郵件：<input type="email" v-model="editData.email"></p>
          <div class="button-container">
            <button class="save" @click="saveProfile">保存</button>
            <button class="cancel" @click="cancelEdit">取消</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      userData: {
        username: '示例用戶',
        email: 'example@example.com',
        phone: '123-456-7890',
        department_id: '示例部門',
        position_id: '示例職位'
      },
      editData: {},
      isSidebarOpen: false,
      isEditing: false
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
    },
    editProfile() {
      this.editData = { ...this.userData };
      this.isEditing = true;
    },
    cancelEdit() {
      this.isEditing = false;
    },
    saveProfile() {
      this.userData = { ...this.editData };
      this.isEditing = false;
      alert('個人信息已更新');
    }
  }
};
</script>

<style src="../assets/css/ProfilePage.css"></style>
