<template>
  <div class="container">
    <div class="header">
      <h2>用戶管理</h2>
      <button id="pending-approval-btn" class="pending-approval-btn" @click="navigateToPendingList">待審核</button>
    </div>
    <div class="filter-section">
      <label for="sort-select">排序:</label>
      <select id="sort-select" v-model="sortBy" @change="applyFilters">
        <option value="name">姓名</option>
        <option value="email">電子郵件</option>
        <option value="department">部門</option>
        <option value="position">職位</option>
        <option value="creation-time">建立時間</option>
        <option value="last-login">最近登入時間</option>
      </select>
      <label for="department-select">部門:</label>
      <select id="department-select" v-model="departmentFilter" @change="applyFilters">
        <option value="all">全部</option>
        <option v-for="department in departments" :key="department" :value="department">{{ department }}</option>
      </select>
      <input type="text" id="search-box" placeholder="搜尋..." v-model="query" @keydown.enter="applyFilters">
      <button @click="applyFilters" class="search-btn">搜尋</button>
    </div>
    <table class="user-table">
      <thead>
        <tr>
          <th>姓名</th>
          <th>電子郵件</th>
          <th>電話號碼</th>
          <th>部門</th>
          <th>職位</th>
          <th>建立時間</th>
          <th>最近登入時間</th>
          <th>操作</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in filteredUsers" :key="user.id">
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.phone }}</td>
          <td>{{ user.department_id }}</td>
          <td>{{ user.position_id }}</td>
          <td>{{ user.date_joined }}</td>
          <td>{{ user.last_login }}</td>
          <td>
            <button class="edit-btn" @click="navigateToEditUser(user.id)">編輯</button>
            <button class="delete-btn" @click="deleteUser(user.id)">刪除</button>
            <button class="assigning-roles-btn" @click="navigateToAssignRole(user.id)">分配角色</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: 'UserManagement',
  data() {
    return {
      sortBy: 'name',
      departmentFilter: 'all',
      query: '',
      users: [],
      departments: ["銷售部", "人力資源部", "資訊部", "業務部", "財務部"]
    };
  },
  computed: {
    filteredUsers() {
      let filtered = this.users;
      if (this.departmentFilter !== 'all') {
        filtered = filtered.filter(user => user.department_id === this.departmentFilter);
      }
      if (this.query) {
        const queryLowerCase = this.query.toLowerCase();
        filtered = filtered.filter(user => 
          user.username.toLowerCase().includes(queryLowerCase) ||
          user.email.toLowerCase().includes(queryLowerCase) ||
          user.phone.toLowerCase().includes(queryLowerCase)
        );
      }
      return filtered.sort((a, b) => {
        if (this.sortBy === 'name') {
          return a.username.localeCompare(b.username);
        } else if (this.sortBy === 'email') {
          return a.email.localeCompare(b.email);
        } else if (this.sortBy === 'department') {
          return a.department_id.localeCompare(b.department_id);
        } else if (this.sortBy === 'position') {
          return a.position_id.localeCompare(b.position_id);
        } else if (this.sortBy === 'creation-time') {
          return new Date(a.date_joined) - new Date(b.date_joined);
        } else if (this.sortBy === 'last-login') {
          return new Date(a.last_login) - new Date(b.last_login);
        }
        return 0;
      });
    }
  },
  methods: {
    applyFilters() {
      console.log('Filters applied');
    },
    handleSearch(event) {
      if (event.key === 'Enter') {
        this.applyFilters();
      }
    },
    navigateToPendingList() {
      this.$router.push('/management/pending_list');
    },
    navigateToEditUser(userId) {
      this.$router.push(`/management/edit_user/${userId}`);
    },
    navigateToAssignRole(userId) {
      this.$router.push(`/management/assign_role/${userId}`);
    },
    fetchUsers() {
      axios.get('/api/users/')
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.error('Error fetching users:', error);
        });
    },
    deleteUser(userId) {
      if (confirm('確定要刪除此用戶嗎？')) {
        axios.post(`/backend/delete_user/${userId}/`)
          .then(() => {
            this.fetchUsers();
          })
          .catch(error => {
            console.error('Error deleting user:', error);
          });
      }
    }
  },
  mounted() {
    this.fetchUsers();
  }
};
</script>

<style scoped src="../assets/css/UserManagement.css"></style>
