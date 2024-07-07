<template>
  <div class="account-settings">
    <h2>帳號設定</h2>

    <!-- 修改密碼表單 -->
    <form @submit.prevent="changePassword">
      <h3>修改密碼</h3>
      <div>
        <label for="oldPassword">舊密碼：</label>
        <input type="password" id="oldPassword" v-model="passwords.oldPassword" required>
      </div>
      <div>
        <label for="newPassword">新密碼：</label>
        <input type="password" id="newPassword" v-model="passwords.newPassword" required>
      </div>
      <div>
        <label for="confirmPassword">確認新密碼：</label>
        <input type="password" id="confirmPassword" v-model="passwords.confirmPassword" required>
      </div>
      <button type="submit">確認修改密碼</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      passwords: {
        oldPassword: '',
        newPassword: '',
        confirmPassword: ''
      }
    };
  },
  methods: {
    changePassword() {
      // 檢查新密碼和確認新密碼是否一致
      if (this.passwords.newPassword !== this.passwords.confirmPassword) {
        alert('新密碼和確認新密碼不一致');
        return;
      }

      // 這裡可以實現修改密碼的邏輯，例如呼叫 API 更新密碼

      // 清空表單
      this.passwords.oldPassword = '';
      this.passwords.newPassword = '';
      this.passwords.confirmPassword = '';

      alert('密碼修改成功');
    }
  }
};
</script>

<style scoped>
.account-settings {
  max-width: 600px; /* 調整框框的最大寬度 */
  margin: 20px auto; /* 上下間距為 20px，左右自動調整居中 */
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 12px;
}

form {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  color: #f5f2f2; /* 設置 label 文字顏色 */
  font-size: 16px;
}

h2 {
  font-size: 20px;
}

h3 {
  font-size: 18px;
}

input[type="password"] {
  width: calc(100% - 16px); /* 輸入框寬度減去內部 padding 大小 */
  padding: 8px;
  margin-bottom: 10px;
}

button {
  padding: 10px 20px;
  background-color: #007BFF;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 15px;
}
</style>
