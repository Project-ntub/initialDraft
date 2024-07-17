<template>
    <div class="container">
      <div class="header">
        <h2>儀表板管理</h2>
        <div class="buttons">
          <button>新增圖表</button>
          <button>編輯圖表</button>
        </div>
      </div>
      <div class="chart-grid">
        <div class="chart">
          <h3>銷售額</h3>
          <canvas id="salesChart"></canvas>
        </div>
        <div class="chart">
          <h3>營業額</h3>
          <canvas id="usersChart"></canvas>
        </div>
        <div class="chart">
          <h3>庫存量</h3>
          <canvas id="storageChart"></canvas>
        </div>
        <div class="chart">
          <h3>其他圖表</h3>
          <canvas id="otherChart"></canvas>
        </div>
      </div>
    </div>
  </template>
  
<script>
  import { ref, onMounted } from 'vue';
  import { Chart } from 'chart.js';
  
  export default {
    name: 'AppDashboard',
    setup() {
      const myChart = ref(null);
  
      onMounted(() => {
        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
              label: '# of Votes',
              data: [12, 19, 3, 5, 2, 3],
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
              ],
              borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
              ],
              borderWidth: 1
            }]
          },
          options: {
            scales: {
              y: {
                beginAtZero: true
              }
            }
          }
        });
      });
  
      return {
        myChart
      };
    }
  };
  </script>
  
  <style scoped>
  body {
    font-family: Arial, sans-serif;
    background-color: #f0f2f5;
}
.navbar {
    background-color: #007BFF;
    color: white;
    padding: 10px;
}
.container {
    padding: 20px;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.header h2 {
    margin: 0;
}
.header .buttons {
    display: flex;
    gap: 10px;
}
.buttons button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
}
.chart-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
    margin-top: 20px;
}
.chart {
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}
  </style>