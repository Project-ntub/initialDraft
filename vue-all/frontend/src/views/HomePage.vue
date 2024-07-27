<template>
    <div class="home-page">
      <!-- 侧边栏组件 -->
      <SidebarPage @toggleSidebar="handleSidebarToggle" />
      <div class="main-panel">
        <!-- 顶部导航栏组件 -->
        <TopNavbar @export="exportChart" />
        <div class="chart-controls">
          <!-- 控制不同图表显示的按钮 -->
          <button @click="setCurrentChart('RevenueChart')">營業額</button>
          <button @click="setCurrentChart('SalesChart')">銷售額</button>
          <button @click="setCurrentChart('InventoryChart')">庫存量</button>
        </div>
        <div class="chart-container">
          <!-- 动态组件，根据 currentChart 的值渲染相应的组件 -->
          <component :is="currentChart" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  // 引入所需组件
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
        // 默认显示的图表组件
        currentChart: 'SalesChart',
      };
    },
    methods: {
      // 更新 currentChart 的值，以切换到不同的图表组件
      setCurrentChart(chart) {
        this.currentChart = chart;
      },
      handleSidebarToggle(isExpanded) {
        this.isSidebarExpanded = isExpanded;
      },
      // 导出图表数据
      exportChart(type) {
        if (type === 'pdf') {
          this.exportAsPDF();
        } else if (type === 'excel') {
          this.exportAsExcel();
        }
      },
      // 导出图表为 PDF
      exportAsPDF() {
        const doc = new jsPDF();
        const canvas = this.$el.querySelector('.chart-container canvas');
        if (canvas) {
          const imgData = canvas.toDataURL('image/png');
          doc.addImage(imgData, 'PNG', 10, 10);
          doc.save('chart.pdf');
        }
      },
      // 导出图表为 Excel
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
      }
    }
  };
  </script>
  
  <style scoped>
  .home-page {
    display: flex;
    transition: margin-left 0.3s;
  }
  
  .sidebar-expanded .main-panel {
    margin-left: 200px; /* 与侧边栏展开时的宽度匹配 */
  }
  
  .main-panel {
    flex-grow: 1;
    padding: 20px;
    margin-left: 60px; /* 与侧边栏收起时的宽度匹配 */
  }
  
  .chart-controls {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    margin-top: 35px; /* 添加顶部外边距 */
  }
  
  .chart {
    height: 400px; /* 设置图表高度 */
  }
  </style>
  