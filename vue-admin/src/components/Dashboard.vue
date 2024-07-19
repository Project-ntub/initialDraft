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
// import '../assets/Dashboard.css';
import { ref, onMounted } from 'vue';
import { Chart, registerables } from 'chart.js';

Chart.register(...registerables);

export default {
  name: 'AppDashboard',
  setup() {
    const salesChart = ref(null);
    const usersChart = ref(null);
    const storageChart = ref(null);
    const otherChart = ref(null);

    onMounted(() => {
      const salesCtx = document.getElementById('salesChart').getContext('2d');
      new Chart(salesCtx, {
        type: 'line',
        data: {
          labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
          datasets: [{
            label: 'Sales',
            data: [120, 190, 30, 50, 20, 30, 70],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          }]
        }
      });

      const usersCtx = document.getElementById('usersChart').getContext('2d');
      new Chart(usersCtx, {
        type: 'line',
        data: {
          labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
          datasets: [{
            label: 'Users',
            data: [300, 400, 350, 500, 600, 700, 800],
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }]
        }
      });

      const storageCtx = document.getElementById('storageChart').getContext('2d');
      new Chart(storageCtx, {
        type: 'bar',
        data: {
          labels: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
          datasets: [{
            label: 'Storage',
            data: [50, 75, 60, 90, 100, 110, 120],
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 1
          }]
        }
      });

      const otherCtx = document.getElementById('otherChart').getContext('2d');
      new Chart(otherCtx, {
        type: 'doughnut',
        data: {
          labels: ['Media', 'Document', 'Others'],
          datasets: [{
            label: 'File Types',
            data: [50, 30, 20],
            backgroundColor: [
              'rgba(255, 206, 86, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
              'rgba(255, 206, 86, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
          }]
        }
      });
    });

    return {
      salesChart,
      usersChart,
      storageChart,
      otherChart
    };
  }
};
</script>

<style scoped src="../assets/css/Dashboard.css"></style>
