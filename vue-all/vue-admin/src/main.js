import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from './axios'; // 確保你正確地匯入了 axios 實例

const app = createApp(App);

app.use(router);
app.use(store);
app.config.globalProperties.$axios = axios; // 將 axios 實例掛載到全域屬性中

app.mount('#app');
