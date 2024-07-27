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
    width: 70px; /* 设置按钮的宽度 */
    padding: 10px; /* 设置按钮的内边距 */
    background-color: #007bff; /* 按钮背景色 */
    color: white; /* 按钮文字颜色 */
    border: none; /* 移除按钮边框 */
    border-radius: 5px; /* 设置按钮圆角 */
    cursor: pointer; /* 鼠标悬停时显示为手型指针 */
    font-size: 16px; /* 设置按钮文字大小 */
    transition: background-color 0.3s; /* 设置背景色过渡效果 */
  }
  </style>
  