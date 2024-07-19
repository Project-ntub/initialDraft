import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Management from '../components/Management.vue';
import Dashboard from '../components/Dashboard.vue';
import UserManagement from '../components/UserManagement.vue';
import RoleManagement from '../components/RoleManagement.vue';

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  {
    path: '/management',
    component: Management,
    children: [
      { path: 'dashboard', component: Dashboard },
      { path: 'UserMmanagement', component: UserManagement },
      { path: 'RoleManagement', component: RoleManagement },
      // 這裡可以添加更多子路由，如 role-management 等
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
