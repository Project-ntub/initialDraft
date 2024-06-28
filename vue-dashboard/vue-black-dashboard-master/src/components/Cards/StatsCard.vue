<template>
  <!-- StatsCard component: 統計卡片組件 -->
  <card>
    <div>
      <div class="row">
        <!-- Header slot: 頭部插槽 -->
        <div class="col-5" v-if="$slots.header">
          <slot name="header"></slot>
        </div>
        <!-- Content slot: 內容插槽 -->
        <div class="col-7" v-if="$slots.content">
          <slot name="content"></slot>
        </div>
      </div>
      <!-- Footer slot: 底部插槽 -->
      <div v-if="$slots.footer">
        <hr />
        <slot name="footer"></slot>
      </div>
    </div>
  </card>
</template>

<script>
import Card from "./Card.vue";

export default {
  name: "stats-card",
  components: {
    Card,
  },
};
</script>

<style>
/* Custom styles for the stats-card component can be added here */
/* 可以在這裡添加統計卡片組件的自定義樣式 */
</style>
