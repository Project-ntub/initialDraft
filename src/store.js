// src/store.js
import { reactive } from 'vue';

export const store = reactive({
  fontSize: 'medium', // 默认字体大小
  setFontSize(size) {
    this.fontSize = size;
  }
});
