import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '@/views/LoginPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';
import ForgetPasswordPage from '@/views/ForgetPasswordPage.vue';
import HomePage from '@/views/HomePage.vue';
import ProfilePage from '@/views/ProfilePage.vue';
import AccountSettings from '@/views/AccountSettings.vue'; 
import ChangePassword from '@/views/ChangePassword.vue';
import PreferenceSetting from '@/views/PreferenceSetting.vue';
import HistoryPage from '@/views/HistoryPage.vue';
import HistoryDetails from '@/views/HistoryDetails.vue'; 

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', name: 'Login', component: LoginPage, meta: { hideNavbar: true, hideSidebar: true } },
  { path: '/register', name: 'Register', component: RegisterPage, meta: { hideNavbar: true, hideSidebar: true } },
  { path: '/forgetpassword', name: 'ForgetPassword', component: ForgetPasswordPage, meta: { hideNavbar: true, hideSidebar: true } },
  { path: '/home', name: '首頁', component: HomePage },
  { path: '/profile', name: '個人資訊', component: ProfilePage },
  { path: '/accountsettings', name: '帳號設定', component: AccountSettings },
  { path: '/changepassword', name: '修改密碼', component: ChangePassword },
  { path: '/preferences', name: '偏好設定', component: PreferenceSetting },
  { path: '/historydetails', name: '歷史紀錄詳情', component: HistoryDetails },
  { path: '/detail/:id', name: '歷史紀錄詳情', component: HistoryDetails },
  { path: '/history', name: '歷史紀錄', component: HistoryPage },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
