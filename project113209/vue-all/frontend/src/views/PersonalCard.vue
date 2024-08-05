<template>
  <div class="personal-card-page">
    <!-- 使用 Sidebar 组件 -->
    <SidebarPage /> <!-- 这里使用 SidebarPage 组件 -->
    <div class="main-panel">
      <div class="personal-card">
        <img :src="userData?.avatar || 'https://via.placeholder.com/150'" alt="Avatar">
        <h2>{{ userData?.name }}</h2>
        <h3>{{ userData?.position }}</h3>
        <p>{{ userData?.department }}</p>
        <p>{{ userData?.email }}</p>
        <p>{{ userData?.phone }}</p>
        <button class="edit-button" @click="editUser">編輯</button>
      </div>
    </div>
  </div>
</template>

<script>
import SidebarPage from '@/components/SidebarPage.vue'; // 导入 SidebarPage 组件

export default {
  name: 'PersonalCard',
  components: {
    SidebarPage, // 注册 SidebarPage 组件
  },
  data() {
    return {
      userData: {
        avatar: '',
        name: '用戶名',
        position: '職位',
        department: '部門',
        email: 'email@example.com',
        phone: '123-456-7890'
      }
    };
  },
  methods: {
    editUser() {
      alert('編輯按鈕被點擊');
    }
  }
};
</script>

<style scoped src="../assets/css/PersonalCard.css"></style>
