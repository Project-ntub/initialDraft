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
        // Implement your filtering logic here
        console.log('Filters applied');
      },
      handleSearch(event) {
        if (event.key === 'Enter') {
          this.applyFilters();
        }
      },
      navigateToPendingList() {
        this.$router.push('/pending_list');
      },
      navigateToEditUser(userId) {
        this.$router.push(`/edit_user/${userId}`);
      },
      deleteUser(userId) {
        // Implement your delete logic here
        console.log(`Delete user with ID: ${userId}`);
      },
      navigateToAssignRole(userId) {
        this.$router.push(`/assign_role/${userId}`);
      }
    },
    mounted() {
      // Fetch the users from the backend or pass them as props
      this.users = [
        // Sample data
        { id: 1, username: 'John Doe', email: 'john@example.com', phone: '123456789', department_id: '銷售部', position_id: '經理', date_joined: '2023-01-01', last_login: '2023-01-10' },
        // Add more sample users here
      ];
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
    align-items: flex-start;
    min-height: 100vh;
  }
  
  .container {
    width: 90%;
    margin: 20px auto;
    background-color: #ffffff;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 8px;
  }
  
  .header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
    justify-content: space-between;
    flex-wrap: wrap;
  }
  
  .pending-approval-btn {
    background-color: #4CAF50;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    color: white;
    text-align: center;
  }
  
  .pending-approval-btn:hover {
    background-color: #45a049;
  }
  
  .filter-section label, .filter-section select, .filter-section input {
    margin-right: 10px;
    margin-bottom: 10px;
  }
  
  .user-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 10px;
  }
  
  .user-table th, .user-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  .user-table th {
    background-color: #f2f2f2;
  }
  
  .user-table tr:nth-child(even) {
    background-color: #f9f9f9;
  }
  
  .user-table tr:hover {
    background-color: #ddd;
  }
  
  .edit-btn, .delete-btn, .assigning-roles-btn {
    padding: 5px 10px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    color: white;
    text-align: center;
    text-decoration: none;
  }
  
  .edit-btn {
    background-color: #ffa500;
  }
  
  .edit-btn:hover {
    background-color: #e59400;
  }
  
  .delete-btn {
    background-color: #f44336;
  }
  
  .delete-btn:hover {
    background-color: #d32f2f;
  }
  
  .assigning-roles-btn {
    background-color: #2196F3;
  }
  
  .assigning-roles-btn:hover {
    background-color: #1976D2;
  }
  
  /* Add responsive design */
  @media (max-width: 768px) {
    .header {
      flex-direction: column;
      align-items: flex-start;
    }
  
    .user-table th, .user-table td {
      padding: 6px;
    }
  
    .edit-btn, .delete-btn, .assigning-roles-btn {
      padding: 3px 5px;
    }
  }
  </style>
  