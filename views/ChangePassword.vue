<template>
  <div class="change-password-container">
    <h2>修改密碼</h2>
    <form @submit.prevent="handleChangePassword">
      <div class="input-group">
        <label for="currentPassword">原密碼</label>
        <input type="password" id="currentPassword" v-model="currentPassword" required />
      </div>
      <div class="input-group">
        <label for="newPassword">新密碼</label>
        <input type="password" id="newPassword" v-model="newPassword" required />
      </div>
      <div class="input-group">
        <label for="confirmNewPassword">確認新密碼</label>
        <input type="password" id="confirmNewPassword" v-model="confirmNewPassword" required />
      </div>
      <button type="submit" class="submit-button">更改密碼</button>
      <button type="button" class="cancel-button" @click="cancelChanges">取消變更</button>
      <div id="feedback" class="feedback">{{ feedback }}</div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentPassword: '',
      newPassword: '',
      confirmNewPassword: '',
      feedback: ''
    };
  },
  methods: {
    handleChangePassword() {
      if (this.newPassword !== this.confirmNewPassword) {
        this.feedback = '新密碼與確認密碼不匹配';
      } else {
        this.feedback = '密碼已更改';
      }
    },
    cancelChanges() {
      this.feedback = '您取消了變更密碼';
    }
  }
};
</script>

<style scoped>
.change-password-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 1em;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
}
.input-group {
  margin-bottom: 1em;
}
.submit-button, .cancel-button {
  display: inline-block;
  margin-right: 10px;
}
.feedback {
  margin-top: 1em;
  color: red;
}
</style>
