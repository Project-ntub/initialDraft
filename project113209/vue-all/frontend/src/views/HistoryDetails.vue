<template>
    <div class="history-details">
      <!-- <div class="header">歷史紀錄詳情</div> -->
      <div class="container">
        <div class="details-container" v-if="detail">
          <h2>{{ detail.timestamp }}</h2>
          <div class="details-content">
            <p>操作：{{ detail.action }}</p>
            <p>時間：{{ detail.timestamp }}</p>
            <p>使用者：{{ detail.user }}</p>
            <p v-if="detail.device">設備品牌：{{ detail.device.brand }}</p>
            <p v-if="detail.device">設備類型：{{ detail.device.type }}</p>
            <p>操作結果：{{ detail.success ? '成功' : '失敗' }}</p>
          </div>
        </div>
        <div v-else>
          <p>未找到該紀錄的詳細信息。</p>
        </div>
        <div class="back-btn">
          <button @click="goBack">返回上一頁</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        details: [
          {
            id: 1,
            timestamp: '2024/1/22 16:22:39',
            action: '編輯個人資訊',
            user: 'User1',
            device: {
              brand: 'Dell',
              type: 'PC'
            },
            success: true
          },
          {
            id: 2,
            timestamp: '2024/1/22 16:00:21',
            action: '查看首頁',
            user: 'User2',
            device: {
              brand: 'Apple',
              type: '平板'
            },
            success: false
          },
          {
            id: 3,
            timestamp: '2024/7/12 22:03',
            action: '登入',
            user: 'User3',
            device: {
              brand: 'Samsung',
              type: '手機'
            },
            success: true
          }
          
          
          // 其他紀錄略
        ],
        detail: null
      };
    },
    mounted() {
      const id = parseInt(this.$route.params.id);
      this.detail = this.details.find(item => item.id === id) || { error: '未找到該紀錄的詳細信息。' };
    },
    methods: {
      goBack() {
        this.$router.go(-1);
      }
    }
  };
  </script>
  
  <style scoped>
  .history-details {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    margin: 0;
    padding: 0;
  }
  .header {
    background-color: black;
    color: white;
    padding: 10px;
    text-align: center;
    border-radius: 5px 5px 0 0;
  }
  .container {
    width: 600px;
    margin: 0 auto;
    padding-top: 50px;
  }
  .details-container {
    background-color: #fff;
    padding: 20px;
    border: 1px solid #d4d4d4;
    border-radius: 5px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
    margin-top: 20px;
  }
  .details-container h2 {
    color: #3f51b5;
  }
  .details-content {
    margin-top: 10px;
  }
  .details-content p {
    margin: 0;
  }
  .back-btn {
    margin-top: 20px;
    text-align: center;
  }
  .back-btn button {
    background-color: #007bff;
    color: white;
    padding: 10px 16px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  .back-btn button:hover {
    background-color: #0056b3;
  }
  </style>
  