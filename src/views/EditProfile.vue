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
  props: ['userData'],
  data() {
    return {
      showEdit: false,
      localData: { ...this.userData }
    };
  },
  methods: {
    toggleEdit() {
      this.showEdit = !this.showEdit;
    },
    saveProfile() {
      this.$emit('updateProfile', this.localData);
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
  display: flex; /* 使用 flex 布局 */
  justify-content: flex-start; /* 水平对齐到左边 */
  align-items: flex-start; /* 垂直对齐到上边 */
  padding: 20px; /* 内边距 */
  gap: 20px; /* 元素之间的间距 */
  margin-top: 20px; /* 添加顶部外边距，避免被顶部导航栏遮挡 */
}

.profile-card-container {
  margin-top: 20px; /* 个人卡片的顶部外边距 */
}

.edit-profile-container {
  background-color: #fff; /* 设置背景为白色 */
  padding: 20px; /* 内边距 */
  border-radius: 10px; /* 圆角 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* 阴影 */
  width: 100%; /* 设定宽度 */
  max-width: 700px; /* 最大宽度 */
  margin-top: 100px auto; /* 居中 */
}

.input-group-container {
  display: flex; /* 使用 flex 布局 */
  gap: 20px; /* 元素之间的间距 */
  margin-bottom: 20px; /* 下方边距 */
}

.input-group {
  flex: 1;
}

label {
  display: block; /* 设置为块级元素 */
  margin-bottom: 5px; /* 下方边距 */
  font-weight: bold; /* 加粗字体 */
}

input {
  width: 100%; /* 全宽 */
  padding: 10px; /* 内边距 */
  border: 1px solid #ccc; /* 边框 */
  border-radius: 5px; /* 圆角 */
  box-sizing: border-box; /* 包括内边距和边框 */
}

.button-container {
  display: flex; /* 使用 flex 布局 */
  justify-content: space-between; /* 两个按钮之间的距离 */
  margin-top: 20px; /* 上方边距 */
}

.save-button, .cancel-button {
  padding: 10px 20px; /* 填充 */
  border: none; /* 无边框 */
  border-radius: 5px; /* 圆角 */
  cursor: pointer; /* 鼠标样式 */
}

.save-button {
  background-color: #6200ea; /* 背景色 */
  color: white; /* 字体颜色 */
}

.cancel-button {
  background-color: #ccc; /* 背景色 */
  color: white; /* 字体颜色 */
}

.save-button:hover {
  background-color: #3700b3; /* 悬停背景色 */
}

.cancel-button:hover {
  background-color: #999; /* 悬停背景色 */
}
</style>
