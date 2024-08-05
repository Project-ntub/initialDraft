<template>
    <div>
      <canvas ref="chartCanvas"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart as ChartJS, Title, Tooltip, Legend, LineController, LineElement, PointElement, LinearScale, CategoryScale } from 'chart.js'
  ChartJS.register(Title, Tooltip, Legend, LineController, LineElement, PointElement, LinearScale, CategoryScale)
  
  export default {
    name: 'ChartComponent',
    props: {
      chartData: {
        type: Object,
        required: true
      }
    },
    mounted() {
      this.renderChart()
    },
    methods: {
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
  