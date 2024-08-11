<template>
  <div>
    <h2>重設密碼</h2>
    <form @submit.prevent="resetPassword">
      <input type="hidden" v-model="uid" />
      <input type="hidden" v-model="token" />
      <label for="password">新密碼</label>
      <input type="password" v-model="password" required />
      <label for="passwordConfirm">確認新密碼</label>
      <input type="password" v-model="passwordConfirm" required />
      <button type="submit">重設密碼</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      uid: this.$route.query.uid,
      token: this.$route.query.token,
      password: '',
      passwordConfirm: '',
      message: ''
    };
  },
  methods: {
    async resetPassword() {
      if (this.password !== this.passwordConfirm) {
        this.message = '密碼不匹配。';
        return;
      }

      try {
        const response = await this.$http.post('/api/password_reset/confirm/', {
          uid: this.uid,
          token: this.token,
          new_password: this.password
        });
        this.message = '密碼已重設成功。';
      } catch (error) {
        this.message = '重設失敗，請重試。';
      }
    }
  }
};
</script>

<style scoped src="../assets/css/ResetPasswordPage.css"></style>
