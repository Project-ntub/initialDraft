<template>
    <div class="history-record">
      <h2>歷史紀錄</h2>
      <table>
        <thead>
          <tr>
            <th>日期</th>
            <th>時間</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="record in records" :key="record.id">
            <td>{{ record.date }}</td>
            <td>{{ record.time }}</td>
            <td>{{ record.action }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HistoryRecord',
    data() {
      return {
        records: [
          { id: 1, date: '2024-06-28', time: '10:00', action: '登入' },
          { id: 2, date: '2024-06-28', time: '10:30', action: '修改個人資訊' },
          { id: 3, date: '2024-06-28', time: '11:00', action: '登出' },
          // 更多記錄可以在這裡添加
        ],
      };
    },
  };
  </script>
  
  <style scoped>
  .history-record {
    padding: 20px;
  }
  
  .history-record table {
    width: 100%;
    border-collapse: collapse;
  }
  
  .history-record th,
  .history-record td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  .history-record th {
    background-color: #f2f2f2;
  }
  </style>
  