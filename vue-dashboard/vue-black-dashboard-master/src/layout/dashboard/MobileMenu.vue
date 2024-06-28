<template>
  <!-- 定義了一個模板部分，包含一個 ul 元素，類名為 nav navbar-nav nav-mobile-menu -->
  <ul class="nav navbar-nav nav-mobile-menu">
    <!-- 在 ul 元素中使用了插槽，插入的內容由外部組件決定 -->
    <slot></slot>
  </ul>
</template>

<script>
export default {};
// 導出一個空的 Vue 組件定義
</script>

<style></style>
// 空的樣式部分，這裡沒有定義任何樣式
