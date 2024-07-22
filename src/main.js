// main.js
import { createApp } from 'vue';
import App from './App.vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { fas } from '@fortawesome/free-solid-svg-icons';
import router from './router';

// 将所有图标添加到库中
library.add(fas);

// 创建 Vue 应用
const app = createApp(App);

// 注册 FontAwesomeIcon 组件
app.component('font-awesome-icon', FontAwesomeIcon);

// 使用 router
app.use(router);

// 挂载应用
app.mount('#app');
