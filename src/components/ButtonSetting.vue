<template>
    <div class="button-setting">
      <button @click="showChart('sales')">銷售額</button>
      <button @click="showChart('revenue')">營業額</button>
      <button @click="showChart('inventory')">庫存量</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'ButtonSetting',
    methods: {
      showChart(chartType) {
        this.$emit('show-chart', chartType);
      }
    }
  }
  </script>
  
  <style scoped>
  .button-setting {
    text-align: center;
    margin-top: 20px;
  }
  .button-setting button {
    margin: 5px;
  }
  </style>
  