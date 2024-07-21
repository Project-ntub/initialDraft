import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Management from '../components/Management.vue';
import Dashboard from '../components/Dashboard.vue';
import UserManagement from '../components/UserManagement.vue';
import RoleManagement from '../components/RoleManagement.vue';
import PendingList from '../components/PendingList.vue';
import EditUser from '../components/EditUser.vue'; // 確保導入EditUser組件

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  {
    path: '/management',
    component: Management,
    children: [
      { path: 'dashboard', component: Dashboard },
      { path: 'user-management', component: UserManagement },
      { path: 'role-management', component: RoleManagement },
      { path: 'pending_list', component: PendingList },
      { path: 'edit_user/:userId', component: EditUser }, // 新增路由
      // 其他子路由...
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
