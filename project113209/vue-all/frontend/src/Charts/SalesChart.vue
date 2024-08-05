<template>
  <div>
    <canvas ref="canvas"></canvas>
  </div>
</template>

<script>
import { Chart } from 'chart.js';

export default {
  props: ['chartData'],
  watch: {
    chartData: {
      immediate: true,
      handler(newData) {
        if (this.chart) {
          this.chart.destroy();
        }
        this.createChart(newData);
      },
    },
  },
  methods: {
    createChart(data) {
      if (!data || !data.labels || !data.datasets) {
        console.error('Invalid chart data:', data);
        return;
      }
      const ctx = this.$refs.canvas.getContext('2d');
      this.chart = new Chart(ctx, {
        type: 'bar', // 假設你使用的是 bar 圖表，根據需要調整
        data: {
          labels: data.labels,
          datasets: data.datasets,
        },
        options: {
          responsive: true,
        },
      });
    },
  },
  mounted() {
    this.createChart(this.chartData);
  },
};
</script>
