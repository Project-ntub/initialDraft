<template>
  <!-- 定義 Vue 單文件組件的模板部分 -->
  <div class="content">
    <!-- 包裹內容的 div 元素，通常用來標示特定的樣式或佈局區域 -->
    <fade-transition :duration="100" mode="out-in">
      <!-- 使用淡入淡出效果的過渡組件 -->
      <!-- router-view 是 Vue Router 提供的內置組件，用於根據路由顯示匹配的內容 -->
      <router-view></router-view>
    </fade-transition>
  </div>
</template>
<script>
// 引入來自 vue2-transitions 模組的 FadeTransition 過渡效果組件
import { FadeTransition } from "vue2-transitions";

export default {
  components: {
    FadeTransition, // 將 FadeTransition 注冊為局部組件
  },
};
</script>

