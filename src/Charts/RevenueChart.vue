<template>
  <div>
    <canvas ref="chartCanvas"></canvas>
  </div>
</template>

<script>
import { Chart as ChartJS, Title, Tooltip, Legend, LineController, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js'
ChartJS.register(Title, Tooltip, Legend, LineController, LineElement, PointElement, LinearScale, CategoryScale)

export default {
  name: 'RevenueChart',
  data() {
    return {
      // 定义图表数据
      chartData: {
        labels: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
        datasets: [
          {
            label: 'Revenue',
            backgroundColor: '#f87979',
            data: [30, 10, 5, 25, 15, 30, 25, 60, 30, 25, 60, 30]
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
