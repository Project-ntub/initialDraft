<template>
  <div class="content">
    <!-- 使用 fade-transition 元件來實現淡入淡出效果，設定過渡時間為 100 毫秒，並指定模式為 out-in -->
    <fade-transition :duration="100" mode="out-in">
      <!-- 在這裡放置你的內容 -->
      <router-view></router-view> <!-- router-view 是 Vue Router 提供的元件，用來渲染匹配到的路由組件 -->
    </fade-transition>
  </div>
</template>

<script>
import { FadeTransition } from "vue2-transitions"; // 導入 vue2-transitions 套件中的 FadeTransition 過渡效果組件

export default {
  components: {
    FadeTransition, // 註冊 FadeTransition 組件
  },
};
</script>
