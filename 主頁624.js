function initRedYellowBlueCharts() {
  createBarChartWithColors('redYellowBlueChart', ['收入', '營業成本', '營業淨利'], 
                           [storeData.sales.value, storeData.revenue.cost, storeData.sales.profit]);
}

function createBarChartWithColors(canvasId, labels, data) {
  const ctx = document.getElementById(canvasId).getContext('2d');
  const chartConfig = {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: '數量',
        data: data,
        backgroundColor: ['#FF6384', '#FFCE56', '#36A2EB'],
        borderColor: ['#FF6384', '#FFCE56', '#36A2EB'],
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
  };
  new Chart(ctx, chartConfig);
}

function showChart(type) {
  document.getElementById('salesChartContainer').style.display = 'none';
  document.getElementById('revenueChartContainer').style.display = 'none';
  document.getElementById('inventoryChartContainer').style.display = 'none';
  document.getElementById('redYellowBlueChartContainer').style.display = 'none'; // 隱藏新圖表容器

  const chartContainerId = type + 'ChartContainer';
  document.getElementById(chartContainerId).style.display = 'block';

  if (type === 'sales') {
    initSalesCharts();
  } else if (type === 'revenue') {
    initRevenueCharts();
  } else if (type === 'inventory') {
    initInventoryCharts();
  } else if (type === 'redYellowBlue') {
    initRedYellowBlueCharts();
  }
}

window.onload = function() {
  showChart('sales'); // 預設顯示銷售額圖表
  populateDateSelects(); // 初始化日期選擇器
  initRedYellowBlueCharts(); // 初始化紅黃藍圖表
}