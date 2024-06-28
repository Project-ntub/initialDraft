<template>
  <!-- 基礎輸入框組件 -->
  <div
    class="form-group"
    :class="{
      'input-group': hasIcon,  // 如果有圖示，添加 input-group 類
      'input-group-focus': focused,  // 如果輸入框聚焦，添加 input-group-focus 類
    }"
  >
    <!-- 標籤插槽，用於顯示輸入框的標籤 -->
    <slot name="label">
      <label v-if="label" class="control-label">
        {{ label }}
      </label>
    </slot>
    
    <!-- 左側附加物插槽，如果有左側圖示，則顯示在輸入框左側 -->
    <slot name="addonLeft">
      <span v-if="addonLeftIcon" class="input-group-prepend">
        <div class="input-group-text">
          <i :class="addonLeftIcon"></i>
        </div>
      </span>
    </slot>
    
    <!-- 默認插槽，用於渲染輸入框 -->
    <slot>
      <input
        :value="value"
        v-bind="$attrs"
        v-on="listeners"
        class="form-control"
        aria-describedby="addon-right addon-left"
      />
    </slot>
    
    <!-- 右側附加物插槽，如果有右側圖示，則顯示在輸入框右側 -->
    <slot name="addonRight">
      <span v-if="addonRightIcon" class="input-group-append">
        <div class="input-group-text">
          <i :class="addonRightIcon"></i>
        </div>
      </span>
    </slot>
    
    <!-- 幫助文本插槽，用於在輸入框下方添加額外的幫助或提示文本 -->
    <slot name="helperText"></slot>
  </div>
</template>

<script>
export default {
  inheritAttrs: false,  // 不繼承父元素的屬性到 input 元素
  name: "base-input",  // 組件名稱
  props: {
    label: {
      type: String,
      description: "輸入框的標籤",  // 輸入框的標籤
    },
    value: {
      type: [String, Number],
      description: "輸入框的值",  // 輸入框的值
    },
    addonRightIcon: {
      type: String,
      description: "右側附加物的圖示",  // 右側附加物的圖示
    },
    addonLeftIcon: {
      type: String,
      description: "左側附加物的圖示",  // 左側附加物的圖示
    },
  },
  model: {
    prop: "value",
    event: "input",
  },
  data() {
    return {
      focused: false,  // 聚焦狀態
    };
  },
  computed: {
    hasIcon() {
      // 檢查是否有左側或右側圖示插槽或者指定的圖示屬性
      const { addonRight, addonLeft } = this.$slots;
      return (
        addonRight !== undefined ||
        addonLeft !== undefined ||
        this.addonRightIcon !== undefined ||
        this.addonLeftIcon !== undefined
      );
    },
    listeners() {
      // 傳遞所有父組件綁定的事件，並添加 input、blur、focus 事件的處理函數
      return {
        ...this.$listeners,
        input: this.onInput,
        blur: this.onBlur,
        focus: this.onFocus,
      };
    },
  },
  methods: {
    onInput(evt) {
      this.$emit("input", evt.target.value);  // 發送輸入事件，將值傳遞給父組件
    },
    onFocus() {
      this.focused = true;  // 當輸入框聚焦時更新聚焦狀態
    },
    onBlur() {
      this.focused = false;  // 當輸入框失去焦點時更新聚焦狀態
    },
  },
};
</script>

<style>
/* 可以在這裡添加 base-input 組件的自定義樣式 */
</style>
