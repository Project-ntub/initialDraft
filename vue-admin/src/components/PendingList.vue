<template>
    <div class="container">
      <a href="/management/user-management" class="back-button">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M15 18L9 12L15 6" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        回到用戶管理
      </a>
      <h1>待審核名單</h1>
      <table class="pending-table">
        <thead>
          <tr>
            <th>姓名</th>
            <th>電子郵件</th>
            <th>電話號碼</th>
            <th>申請時間</th>
            <th>審核</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in pendingUsers" :key="user.id">
            <td>{{ user.username }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.phone }}</td>
            <td>{{ user.date_joined ? user.date_joined : '未知' }}</td>
            <td>
              <form @submit.prevent="approveUser(user.id)">
                <button type="submit" class="approve-btn">開通</button>
              </form>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  import axios from '../axios';
//   import '../assets/pending_list.css'; // 確保文件名大小寫正確
  
  export default {
    name: 'PendingList',
    data() {
      return {
        pendingUsers: []
      };
    },
    methods: {
      fetchPendingUsers() {
        axios.get('/api/pending-users/')
          .then(response => {
            this.pendingUsers = response.data;
          })
          .catch(error => {
            console.error('Error fetching pending users:', error);
          });
      },
      approveUser(userId) {
        axios.post(`/api/approve-user/${userId}/`)
          .then(response => {
            console.log('User approved:', response);
            this.fetchPendingUsers(); // Refresh the list after approval
          })
          .catch(error => {
            console.error('Error approving user:', error);
          });
      }
    },
    mounted() {
      this.fetchPendingUsers();
    }
  };
  </script>
    
    <style scoped src="../assets/css/PendingList.css"></style>
