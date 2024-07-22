<template>
    <div>
      <!-- Search Box -->
      <div class="search-container">
        <input type="text" v-model="searchQuery" placeholder="查尋歷史紀錄...">
        <button @click="searchHistory">查尋</button>
        <button @click="refreshPage">重整</button>
      </div>
  
      <!-- Modal for adding records -->
      <div v-if="isAddRecordModalVisible" class="modal" @click.self="closeModal('addRecordModal')">
        <div class="modal-content">
          <span class="close" @click="closeModal('addRecordModal')">&times;</span>
          <form @submit.prevent="addRecord">
            <label for="userName">用戶:</label>
            <input type="text" v-model="newRecord.userName" required><br><br>
            <label for="userAction">操作:</label>
            <input type="text" v-model="newRecord.userAction" required><br><br>
            <label for="userEmail">電子郵件:</label>
            <input type="email" v-model="newRecord.userEmail" required><br><br>
            <label for="timestamp">操作時間:</label>
            <input type="datetime-local" v-model="newRecord.timestamp" required><br><br>
            <button type="submit">新增紀錄</button>
          </form>
        </div>
      </div>
  
      <!-- History Records Section -->
      <div class="history-container">
        <h2>歷史紀錄</h2>
        <table class="history-table" id="history-table">
          <thead>
            <tr>
              <th>編號</th>
              <th>用戶</th>
              <th>歷史操作</th>
              <th>電子郵件</th>
              <th>操作時間</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(record, index) in filteredRecords" :key="index">
              <td>{{ index + 1 }}</td>
              <td>{{ record.userName }}</td>
              <td>{{ record.userAction }}</td>
              <td>{{ record.userEmail }}</td>
              <td>{{ record.timestamp }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        searchQuery: '',
        isAddRecordModalVisible: false,
        newRecord: {
          userName: '',
          userAction: '',
          userEmail: '',
          timestamp: ''
        },
        records: [
          { userName: '張三', userAction: '新增角色', userEmail: 'zhangsan@example.com', timestamp: '2024-05-30 10:00' },
          { userName: '李四', userAction: '刪除角色', userEmail: 'lisi@example.com', timestamp: '2024-05-30 11:00' }
          // 更多歷史紀錄
        ]
      };
    },
    computed: {
      filteredRecords() {
        return this.records.filter(record => {
          return Object.values(record).some(val => val.toLowerCase().includes(this.searchQuery.toLowerCase()));
        });
      }
    },
    methods: {
      openModal(modalName) {
        if (modalName === 'addRecordModal') {
          this.isAddRecordModalVisible = true;
        }
      },
      closeModal(modalName) {
        if (modalName === 'addRecordModal') {
          this.isAddRecordModalVisible = false;
        }
      },
      addRecord() {
        this.records.push({ ...this.newRecord });
        this.newRecord = { userName: '', userAction: '', userEmail: '', timestamp: '' };
        this.closeModal('addRecordModal');
      },
      searchHistory() {
        // 搜尋功能由 computed: filteredRecords 處理
      },
      refreshPage() {
        window.location.reload();
      }
    },
    mounted() {
      this.collectAndSendData();
    },
    methods: {
      collectAndSendData() {
        // 假設這裡有邏輯收集並發送數據到後端
      }
    }
  };
  </script>
  
  <style scoped>
  .modal {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    overflow: auto;
    background-color: rgba(0,0,0,0.4);
    padding-top: 60px;
  }
  .modal-content {
    background-color: #fefefe;
    margin: auto;
    padding: 20px;
    border: 1px solid #888;
    width: 80%;
  }
  .close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
  }
  .close:hover,
  .close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
  }
  .history-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }
  .history-table th, .history-table td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  .history-table th {
    background-color: #f2f2f2;
  }
  </style>
  