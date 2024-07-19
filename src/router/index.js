// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
 /* eslint-disable */
import Layout from '@/components/Layout.vue'; // 导入布局组件
import HomePage from '@/views/HomePage.vue'; // 导入首页组件
import LoginPage from '@/views/LoginPage.vue'; // 导入登录页组件
import ProfilePage from '@/views/ProfilePage.vue'; // 导入个人资料页组件
import PreferenceSetting from '@/views/PreferenceSetting.vue'; // 导入偏好设置页组件
import AccountSettings from '@/views/AccountSettings.vue'; // 导入账号设置页组件
import HistoryPage from '@/views/HistoryPage.vue'; // 导入历史记录页组件
import ForgetPasswordPage from '@/views/ForgetPasswordPage.vue'; // 导入忘记密码页组件
import RegisterPage from '@/views/RegisterPage.vue'; // 导入注册页组件
import ChangePassword from '@/views/ChangePassword.vue'; // 导入更改密码页组件
import HistoryDetails from '@/views/HistoryDetails.vue'; // 导入历史详情页组件

const routes = [
  {
    path: '/',
    redirect: '/login', // 根路径重定向到登录页
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage,
    meta: { hideSidebar: true }, // 登录页不显示侧边栏
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage,
    meta: { hideSidebar: true }, // 注册页不显示侧边栏
  },
  {
    path: '/forgetpassword',
    name: 'ForgetPassword',
    component: ForgetPasswordPage,
    meta: { hideSidebar: true }, // 忘记密码页不显示侧边栏
  },
   /* eslint-disable */
  {
    path: '/',
    component: Layout, // 使用布局组件包裹以下所有路由
    children: [
      {
        path: '/home',
        name: '首頁',
        component: HomePage, // 首页组件
      },
      {
        path: '/profile',
        name: '個人資訊',
        component: ProfilePage, // 个人资料页组件
      },
      {
        path: '/preferences',
        name: '偏好設定',
        component: PreferenceSetting, // 偏好设置页组件
      },
      {
        path: '/accountsettings',
        name: '帳號設定',
        component: AccountSettings, // 账号设置页组件
      },
      {
        path: '/history',
        name: '歷史紀錄',
        component: HistoryPage, // 历史记录页组件
      },
      {
        path: '/changepassword',
        name: '修改密碼',
        component: ChangePassword, // 更改密码页组件
      },
      {
        path: '/historydetails',
        name: '歷史紀錄詳情',
        component: HistoryDetails, // 历史详情页组件
      },
      {
        path: '/detail/:id',
        name: '歷史紀錄詳情',
        component: HistoryDetails, // 历史详情页组件（带参数）
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
