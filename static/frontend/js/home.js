const storeData = {
  sales: {
    value: 1300000,
    cost: 1000000,
    profit: 400000,
    barData: [200000, 180000, 160000, 140000, 120000]
  },
  revenue: {
    value: 1242089,
    cost: 900887,
    profit: 341201963,
    barData: [300000, 250000, 200000, 150000, 100000]
  },
  inventory: {
    value: 1400000,
    cost: 1100000,
    profit: 300000,
    barData: [250000, 220000, 200000, 170000, 150000]
  }
};

const gaugeOptions = {
  angle: -0.25,
  lineWidth: 0.1,
  radiusScale: 1,
  pointer: {
    length: 0.6,
    strokeWidth: 0.035,
    color: '#000000'
  },
  limitMax: false,
  limitMin: false,
  highDpiSupport: true,
  staticZones: [
    {strokeStyle: "#F03E3E", min: 0, max: 30},
    {strokeStyle: "#FFDD00", min: 30, max: 70},
    {strokeStyle: "#30B32D", min: 70, max: 100}
  ]
};

function createGauge(canvasId, max, value) {
  const target = document.getElementById(canvasId);
  const gauge = new Gauge(target).setOptions(gaugeOptions);
  gauge.maxValue = max;
  gauge.setMinValue(0);
  gauge.animationSpeed = 32;
  gauge.set(value);
}

function createBarChart(canvasId, labels, data) {
  const ctx = document.getElementById(canvasId).getContext('2d');
  const chartConfig = {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [{
        label: '數量',
        data: data,
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
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

  

  const chartContainerId = type + 'ChartContainer';
  document.getElementById(chartContainerId).style.display = 'block';

  if (type === 'sales') {
    initSalesCharts();
  } else if (type === 'revenue') {
    initRevenueCharts();
  } else if (type === 'inventory') {
    initInventoryCharts();
  }
}

function initSalesCharts() {
  createGauge('salesGauge', 2000000, storeData.sales.value);
  createGauge('salesCostGauge', 2000000, storeData.sales.cost);
  createGauge('salesProfitGauge', 500000000, storeData.sales.profit);
  createBarChart('salesBarChart', ['肥料產品A', '肥料產品B', '肥料產品C', '肥料產品D', '肥料產品E'], storeData.sales.barData);
}

function initRevenueCharts() {
  createGauge('revenueGauge', 2000000, storeData.revenue.value);
  createGauge('revenueCostGauge', 2000000, storeData.revenue.cost);
  createGauge('revenueProfitGauge', 500000000, storeData.revenue.profit);
  createBarChart('revenueBarChart', ['肥料產品A', '肥料產品B', '肥料產品C', '肥料產品D', '肥料產品E'], storeData.revenue.barData);
}

function initInventoryCharts() {
  createGauge('inventoryGauge', 2000000, storeData.inventory.value);
  createGauge('inventoryCostGauge', 2000000, storeData.inventory.cost);
  createGauge('inventoryProfitGauge', 500000000, storeData.inventory.profit);
  createBarChart('inventoryBarChart', ['肥料產品A', '肥料產品B', '肥料產品C', '肥料產品D', '肥料產品E'], storeData.inventory.barData);
}

function populateDateSelects() {
  const yearSelect = document.getElementById('yearSelect');
  const monthSelect = document.getElementById('monthSelect');
  const daySelect = document.getElementById('daySelect');

  // 填充年份
  for (let year = 2015; year <= 2025; year++) {
    const option = document.createElement('option');
    option.value = year;
    option.textContent = year;
    yearSelect.appendChild(option);
  }

  // 填充月份
  for (let month = 1; month <= 12; month++) {
    const option = document.createElement('option');
    option.value = month;
    option.textContent = month;
    monthSelect.appendChild(option);
  }

  // 填充日期
  function updateDays() {
    const year = parseInt(yearSelect.value);
    const month = parseInt(monthSelect.value);
    const daysInMonth = new Date(year, month, 0).getDate();
    daySelect.innerHTML = ''; // 清空之前的選項
    for (let day = 1; day <= daysInMonth; day++) {
      const option = document.createElement('option');
      option.value = day;
      option.textContent = day;
      daySelect.appendChild(option);
    }
  }

  yearSelect.addEventListener('change', updateDays);
  monthSelect.addEventListener('change', updateDays);
  updateDays(); // 初始化日期選項
}

function updateChartsByDate() {
  const year = document.getElementById('yearSelect').value;
  const month = document.getElementById('monthSelect').value;
  const day = document.getElementById('daySelect').value;

  console.log(`Selected date: ${year}-${month}-${day}`);
  // 在這裡根據選擇的日期更新圖表數據，這裡假設有一個 fetchDataByDate 函數
  // fetchDataByDate(year, month, day);
}

window.onload = function() {
  showChart('sales'); // 預設顯示銷售額圖表
  populateDateSelects(); // 初始化日期選擇器
}

document.getElementById('yearSelect').addEventListener('change', updateChartsByDate);
document.getElementById('monthSelect').addEventListener('change', updateChartsByDate);
document.getElementById('daySelect').addEventListener('change', updateChartsByDate);
