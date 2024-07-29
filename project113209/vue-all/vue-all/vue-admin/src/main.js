import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import axios from './axios'; // 确保你正确导入了 axios 实例

const app = createApp(App);

app.use(router);
app.use(store);
app.config.globalProperties.$axios = axios; // 将 axios 实例挂载到全局属性中

app.mount('#app');
