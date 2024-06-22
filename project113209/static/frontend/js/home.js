const storeData = {
    'A': { revenue: 100000, trend: [10, 20, 30, 40, 50], inventory: 1000 },
    'B': { revenue: 80000, trend: [15, 25, 35, 45, 55], inventory: 800 },
    'C': { revenue: 120000, trend: [20, 30, 40, 50, 60], inventory: 1200 }
  };

  const charts = {};

  function createChart(canvasId, type, labels, data, label, backgroundColor, borderColor) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    const chartConfig = {
      type: type,
      data: {
        labels: labels,
        datasets: [{
          label: label,
          data: data,
          backgroundColor: backgroundColor,
          borderColor: borderColor,
          borderWidth: 1
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    };

    if (type === 'horizontalBar') {
      chartConfig.type = 'bar';
      chartConfig.options.indexAxis = 'y';
    }

    return new Chart(ctx, chartConfig);
  }

  function showChart(chartId) {
    document.querySelectorAll('.chart-container').forEach(container => container.style.display = 'none');
    document.getElementById(chartId + 'Container').style.display = 'block';
  }

  function showModal() {
    document.getElementById('chartModal').style.display = 'block';
  }

  function closeModal() {
    document.getElementById('chartModal').style.display = 'none';
  }

  function addNewChart() {
    const chartType = document.getElementById('newChartTypeSelect').value;
    const newChartId = `newChart${Object.keys(charts).length + 1}`;
    const newCanvas = document.createElement('canvas');
    newCanvas.id = newChartId;
    newCanvas.classList.add('chart-container');
    document.body.appendChild(newCanvas);

    const newChart = createChart(newChartId, chartType, ['January', 'February', 'March', 'April', 'May'], [12, 19, 3, 5, 2, 3], '新圖表', 'rgba(54, 162, 235, 0.2)', 'rgba(54, 162, 235, 1)');
    charts[newChartId] = newChart;

    closeModal();
  }

  function initDefaultCharts() {
    charts.revenueChart = createChart('revenueChart', 'line', ['January', 'February', 'March', 'April', 'May'], storeData['A'].trend, '營業額', 'rgba(75, 192, 192, 0.2)', 'rgba(75, 192, 192, 1)');
    charts.salesTrendChart = createChart('salesTrendChart', 'line', ['January', 'February', 'March', 'April', 'May'], storeData['B'].trend, '銷售趨勢', 'rgba(153, 102, 255, 0.2)', 'rgba(153, 102, 255, 1)');
    charts.inventoryChart = createChart('inventoryChart', 'line', ['January', 'February', 'March', 'April', 'May'], storeData['C'].trend, '庫存量', 'rgba(255, 159, 64, 0.2)', 'rgba(255, 159, 64, 1)');
  }

  window.onload = function() {
    initDefaultCharts();
    showChart('revenueChart'); // Show the initial chart
  }