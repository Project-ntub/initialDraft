<template>
  <!-- Card component: 卡片組件 -->
  <div class="card" :class="[type && `card-${type}`]">
    <!-- Card image slot: 卡片圖片插槽 -->
    <div class="card-image" v-if="$slots.image">
      <slot name="image"></slot>
    </div>
    <!-- Card header slot: 卡片頭部插槽 -->
    <div class="card-header" v-if="$slots.header || title" :class="headerClasses">
      <slot name="header">
        <!-- Title and subtitle: 標題和副標題 -->
        <h4 class="card-title">{{ title }}</h4>
        <p class="card-category" v-if="subTitle">{{ subTitle }}</p>
      </slot>
    </div>
    <!-- Card body slot: 卡片主體插槽 -->
    <div class="card-body" v-if="$slots.default">
      <slot></slot>
    </div>
    <!-- Card image bottom slot: 卡片底部圖片插槽 -->
    <div class="card-image" v-if="$slots['image-bottom']">
      <slot name="image-bottom"></slot>
    </div>
    <!-- Raw content slot: 原始內容插槽 -->
    <slot name="raw-content"></slot>
    <!-- Card footer slot: 卡片底部插槽 -->
    <div class="card-footer" :class="footerClasses" v-if="$slots.footer">
      <slot name="footer"></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "card",
  props: {
    // Card title: 卡片標題
    title: {
      type: String,
      description: "Card title", // 卡片標題
    },
    // Card subtitle: 卡片副標題
    subTitle: {
      type: String,
      description: "Card subtitle", // 卡片副標題
    },
    // Card type (e.g primary/danger etc): 卡片類型（例如主要/危險等）
    type: {
      type: String,
      description: "Card type (e.g primary/danger etc)", // 卡片類型（例如主要/危險等）
    },
    // Card header css classes: 卡片頭部的 CSS 類
    headerClasses: {
      type: [String, Object, Array],
      description: "Card header css classes", // 卡片頭部的 CSS 類
    },
    // Card body css classes: 卡片主體的 CSS 類
    bodyClasses: {
      type: [String, Object, Array],
      description: "Card body css classes", // 卡片主體的 CSS 類
    },
    // Card footer css classes: 卡片底部的 CSS 類
    footerClasses: {
      type: [String, Object, Array],
      description: "Card footer css classes", // 卡片底部的 CSS 類
    },
  },
};
</script>

<style>
/* Custom styles for the card component can be added here */
/* 可以在這裡添加卡片組件的自定義樣式 */
</style>
