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
.profile-page {
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  padding: 20px;
  gap: 20px;
  margin-top: 60px;
}

.profile-card-container {
  margin-top: 20px;
}

.edit-profile-container {
  background-color: #fff;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  width: 100%;
  max-width: 800px;
  margin: 0 auto;
}

.input-group-container {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
}

.input-group {
  flex: 1;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-sizing: border-box;
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.save-button, .cancel-button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.save-button {
  background-color: #6200ea;
  color: white;
}

.cancel-button {
  background-color: #ccc;
  color: white;
}

.save-button:hover {
  background-color: #3700b3;
}

.cancel-button:hover {
  background-color: #999;
}
</style>
