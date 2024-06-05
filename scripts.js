document.addEventListener('DOMContentLoaded', function () {
    const salesTrendCtx = document.getElementById('sales-trend-chart').getContext('2d');
    const inventoryCtx = document.getElementById('inventory-chart').getContext('2d');
    const revenueCtx = document.getElementById('revenue-line-chart').getContext('2d');

    const salesTrendChart = new Chart(salesTrendCtx, {
        type: 'line',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'Sales Trend',
                data: [65, 59, 80, 81, 56, 55, 40],
                borderColor: 'rgba(75, 192, 192, 1)',
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                fill: true,
                tension: 0.4
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

    const inventoryChart = new Chart(inventoryCtx, {
        type: 'bar',
        data: {
            labels: ['Product A', 'Product B', 'Product C', 'Product D'],
            datasets: [{
                label: 'Inventory',
                data: [20, 30, 40, 50],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
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

    const revenueLineChart = new Chart(revenueCtx, {
        type: 'line',
        data: {
            labels: ['Q1', 'Q2', 'Q3', 'Q4'],
            datasets: [{
                label: 'Revenue',
                data: [15000, 20000, 18000, 22000],
                borderColor: 'rgba(153, 102, 255, 1)',
                backgroundColor: 'rgba(153, 102, 255, 0.2)',
                fill: true,
                tension: 0.4
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

    document.getElementById('chart-select').addEventListener('change', function (e) {
        const selectedChart = e.target.value;

        document.getElementById('sales-trend-chart-container').style.display = 'none';
        document.getElementById('inventory-chart-container').style.display = 'none';
        document.getElementById('revenue-line-chart-container').style.display = 'none';

        document.getElementById(`${selectedChart}-container`).style.display = 'block';
    });

    document.getElementById('add-chart-button').addEventListener('click', function () {
        alert('新增圖表功能待實現');
    });

    document.getElementById('modify-chart-button').addEventListener('click', function () {
        alert('修改圖表功能待實現');
    });
});
