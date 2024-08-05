<template>
  <div class="home-page">
    <SidebarPage @toggleSidebar="handleSidebarToggle" />
    <div class="main-panel">
      <TopNavbar @export="exportChart" />
      <div class="header">
        <div class="dropdown-container">
          <select v-model="selectedBranch" @change="fetchBranchChartData" class="branch-dropdown">
            <option v-for="branch in branches" :key="branch.branch_id" :value="branch.branch_id">
              {{ branch.branch_name }}
            </option>
          </select>
        </div>
      </div>
      <div class="chart-controls">
        <button @click="setCurrentChart('RevenueChart')">營業額</button>
        <button @click="setCurrentChart('SalesChart')">銷售額</button>
        <button @click="setCurrentChart('InventoryChart')">庫存量</button>
      </div>
      <div class="chart-container">
        <component :is="currentChart" :chartData="currentChartData"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import SidebarPage from '@/components/SidebarPage.vue';
import TopNavbar from '@/components/TopNavbar.vue';
import SalesChart from '@/Charts/SalesChart.vue';
import RevenueChart from '@/Charts/RevenueChart.vue';
import InventoryChart from '@/Charts/InventoryChart.vue';
import { jsPDF } from 'jspdf';
import * as XLSX from 'xlsx';
import { saveAs } from 'file-saver';

export default {
  name: 'HomePage',
  components: {
    SidebarPage,
    TopNavbar,
    SalesChart,
    RevenueChart,
    InventoryChart,
  },
  data() {
    return {
      currentChart: 'SalesChart',
      branches: [
        { branch_id: 1, branch_name: '台南武聖' },
        { branch_id: 2, branch_name: '嘉義仁愛' },
        { branch_id: 3, branch_name: '高雄大昌' },
      ],
      selectedBranch: null,
      chartData: [], // 原始 chartData
      parsedChartData: {}, // 解析后的 chartData
    };
  },
  computed: {
    currentChartData() {
      return this.parsedChartData[this.currentChart] || { labels: [], datasets: [] };
    }
  },
  methods: {
    setCurrentChart(chart) {
      this.currentChart = chart;
      this.fetchChartData();
    },
    handleSidebarToggle(isExpanded) {
      this.isSidebarExpanded = isExpanded;
    },
    exportChart(type) {
      if (type === 'pdf') {
        this.exportAsPDF();
      } else if (type === 'excel') {
        this.exportAsExcel();
      }
    },
    exportAsPDF() {
      const doc = new jsPDF();
      const canvas = this.$el.querySelector('.chart-container canvas');
      if (canvas) {
        const imgData = canvas.toDataURL('image/png');
        doc.addImage(imgData, 'PNG', 10, 10);
        doc.save('chart.pdf');
      }
    },
    exportAsExcel() {
      const chartComponent = this.$refs.chartComponent;
      if (chartComponent) {
        const chartData = chartComponent.chartData;
        const worksheet = XLSX.utils.json_to_sheet(chartData.datasets[0].data.map((value, index) => ({
          label: chartData.labels[index],
          value: value
        })));
        const workbook = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(workbook, worksheet, 'Sheet1');
        const excelBuffer = XLSX.write(workbook, { bookType: 'xlsx', type: 'array' });
        const data = new Blob([excelBuffer], { type: 'application/octet-stream' });
        saveAs(data, 'chart.xlsx');
      }
    },
    fetchBranchChartData() {
      if (this.selectedBranch) {
        axios.get(`/frontend/api/chart_data/?branch_id=${this.selectedBranch}`)
          .then(response => {
            this.chartData = response.data;
            this.parseChartData(); // 解析數據
          })
          .catch(error => {
            console.error('Error fetching chart data:', error);
          });
      }
    },
    fetchChartData() {
      axios.get('/frontend/api/chart_data/')
        .then(response => {
          this.chartData = response.data;
          this.parseChartData(); // 解析數據
        })
        .catch(error => {
          console.error('Error fetching chart data:', error);
        });
    },
    parseChartData() {
      // 解析後端返回的數據，轉換為 Chart.js 可用的格式
      const parsedData = {};
      this.chartData.forEach(chart => {
        parsedData[chart.chart_name] = JSON.parse(chart.chart_data);
      });
      this.parsedChartData = parsedData;
    },
  },
};
</script>
