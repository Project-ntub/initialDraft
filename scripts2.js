function createGauge(canvasId, max, value) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    const gaugeContainer = document.createElement('div');
    gaugeContainer.className = 'gauge-container';
  
    gaugeContainer.innerHTML = `
      <div class="button-box">
        <button onclick="changeDataset('revenue', ${max}, ${value})">營業收入</button>
        <button onclick="changeDataset('cost', ${max}, ${value})">營業成本</button>
        <button onclick="changeDataset('profit', ${max}, ${value})">營業淨利</button>
      </div>
      <canvas id="${canvasId}" width="200" height="200"></canvas>
    `;
    
    const chartContainer = document.createElement('div');
    chartContainer.appendChild(gaugeContainer);
    ctx.appendChild(chartContainer);
  }
  function createGauge(canvasId, max, value) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    const gaugeContainer = document.createElement('div');
    gaugeContainer.className = 'gauge-container';
  
    gaugeContainer.innerHTML = `
      <div class="button-box">
        <button onclick="changeDataset('revenue', ${max}, ${value})">營業收入</button>
        <button onclick="changeDataset('cost', ${max}, ${value})">營業成本</button>
        <button onclick="changeDataset('profit', ${max}, ${value})">營業淨利</button>
      </div>
      <canvas id="${canvasId}" width="200" height="200"></canvas>
    `;
    
    const chartContainer = document.createElement('div');
    chartContainer.appendChild(gaugeContainer);
    ctx.appendChild(chartContainer);
  }
  
  function changeDataset(type, max, value) {
    const dataset = {
      revenue: {
        value: 1234567, // Replace with actual revenue value
        backgroundColor: ['#FF6384', '#E0E0E0']
      },
      cost: {
        value: 987654, // Replace with actual cost value
        backgroundColor: ['#36A2EB', '#E0E0E0']
      },
      profit: {
        value: 54321, // Replace with actual profit value
        backgroundColor: ['#FFCE56', '#E0E0E0']
      }
    };
  
    const ctx = document.getElementById(canvasId).getContext('2d');
    const chart = new Chart(ctx, {
      type: 'doughnut',
      data: {
        datasets: [{
          data: [dataset[type].value, max - dataset[type].value],
          backgroundColor: dataset[type].backgroundColor
        }]
      },
      options: {
        responsive: true,
        layout: {
          padding: {
            bottom: 10
          }
        }
      }
    });
  }
    
function populateDateSelects() {
    const yearSelect = document.getElementById('yearSelect');
    const monthSelect = document.getElementById('monthSelect');
    const daySelect = document.getElementById('daySelect');

    for (let year = 2000; year <= 2030; year++) {
      const option = document.createElement('option');
      option.value = year;
      option.textContent = year;
      yearSelect.appendChild(option);
    }
    for (let month = 1; month <= 12; month++) {
        const option = document.createElement('option');
        option.value = month;
        option.textContent = month;
        monthSelect.appendChild(option);
      }

      for (let day = 1; day <= 31; day++) {
        const option = document.createElement('option');
        option.value = day;
        option.textContent = day;
        daySelect.appendChild(option);
      }
    }

    window.onload = function() {
      populateDateSelects();
      showChart('sales');
    };
function updateChartsByDate() {
    const year = document.getElementById('yearSelect').value;
    const month = document.getElementById('monthSelect').value;
    const day = document.getElementById('daySelect').value;
  
    console.log(`Selected date: ${year}-${month}-${day}`);
    // 在這裡根據選擇的日期更新圖表數據，這裡假設有一個 fetchDataByDate 函數
    // fetchDataByDate(year, month, day);
  }
  
  function initQueryButton() {
    const queryButton = document.getElementById('queryButton');
    queryButton.addEventListener('click', updateChartsByDate);
  }
  
  window.onload = function() {
    showChart('sales'); // 預設顯示銷售額圖表
    populateDateSelects(); // 初始化日期選擇器
    initQueryButton(); // 初始化查詢按鈕的點擊事件
  }
  
  document.getElementById('yearSelect').addEventListener('change', updateChartsByDate);
  document.getElementById('monthSelect').addEventListener('change', updateChartsByDate);
  document.getElementById('daySelect').addEventListener('change', updateChartsByDate);
  