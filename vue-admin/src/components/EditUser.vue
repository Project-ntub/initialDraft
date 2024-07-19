<template>
  <div class="container">
    <h2>編輯用戶</h2>
    <form @submit.prevent="updateUser">
      <div class="form-group">
        <label for="username">姓名</label>
        <input type="text" id="username" v-model="user.username" required>
      </div>
      <div class="form-group">
        <label for="email">電子郵件</label>
        <input type="email" id="email" v-model="user.email" required>
      </div>
      <div class="form-group">
        <label for="phone">電話號碼</label>
        <input type="text" id="phone" v-model="user.phone" required>
      </div>
      <div class="form-group">
        <label for="department">部門</label>
        <select id="department" v-model="user.department_id">
          <option value="">選擇部門</option>
          <option v-for="department in departments" :key="department" :value="department">{{ department }}</option>
        </select>
      </div>
      <div class="form-group">
        <label for="position">職位</label>
        <select id="position" v-model="user.position_id">
          <option value="">選擇職位</option>
          <option v-for="position in positions" :key="position" :value="position">{{ position }}</option>
        </select>
      </div>
      <div class="form-group">
        <button type="submit" class="btn-save">儲存</button>
        <button type="button" class="btn-cancel" @click="cancelEdit">取消</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: 'EditUser',
  data() {
    return {
      user: {
        username: '',
        email: '',
        phone: '',
        department_id: '',
        position_id: ''
      },
      departments: ["銷售部", "人力資源部", "資訊部", "業務部", "財務部"],
      positions: ["經理", "主管", "員工"]
    };
  },
  methods: {
    fetchUser() {
      const userId = this.$route.params.userId;
      axios.get(`/api/users/${userId}/`)
        .then(response => {
          this.user = response.data;
        })
        .catch(error => {
          console.error('Error fetching user:', error);
        });
    },
    updateUser() {
      const userId = this.$route.params.userId;
      axios.put(`/api/users/${userId}/`, this.user)
        .then(() => {
          this.$router.push('/management/user-management');
        })
        .catch(error => {
          console.error('Error updating user:', error);
        });
    },
    cancelEdit() {
      this.$router.push('/management/user-management');
    }
  },
  mounted() {
    this.fetchUser();
  }
};
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
.container {
  width: 90%;
  margin: 20px auto;
  background-color: #ffffff;
  padding: 20px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  max-width: 600px;
}
h2 {
  text-align: center;
  margin-bottom: 20px;
}
form {
  display: flex;
  flex-direction: column;
}
.form-group {
  margin-bottom: 15px;
}
label {
  margin-bottom: 5px;
  font-weight: bold;
}
input, select {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  width: 100%;
}
button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
  width: 100px;
  text-align: center;
}
.btn-save {
  background-color: #4CAF50;
  color: white;
}
.btn-save:hover {
  background-color: #45a049;
}
.btn-cancel {
  background-color: #f1f1f1;
  color: black;
  margin-left: 10px;
}
.btn-cancel:hover {
  background-color: #ddd;
}
</style>
