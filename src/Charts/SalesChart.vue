<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { Chart as ChartJS, Title, Tooltip, Legend, LineController, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, LineController, LineElement, PointElement, LinearScale, CategoryScale)

export default {
  name: 'SalesChart',
  data() {
    return {
      // 定义图表数据
      chartData: {
        labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
        datasets: [
          {
            label: 'Sales',
            backgroundColor: '#f87979',
            data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 39, 80, 40]
          }
        ]
      }
    };
  },
  mounted() {
    this.renderChart()
  },
  methods: {
    // 渲染图表
    renderChart() {
      const ctx = this.$refs.chartCanvas.getContext('2d')
      new ChartJS(ctx, {
        type: 'line',
        data: this.chartData,
        options: { responsive: true, maintainAspectRatio: false }
      })
    }
  }
}
</script>

<style scoped>
canvas {
  width: 700px !important;
  height: 400px !important;
}
</style>
