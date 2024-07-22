import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/Login.vue';
import Management from '../components/Management.vue';
import Dashboard from '../components/Dashboard.vue';
import UserManagement from '../components/UserManagement.vue';
import RoleManagement from '../components/RoleManagement.vue';
import PendingList from '../components/PendingList.vue';
import EditUser from '../components/EditUser.vue';
import AssignRole from '@/components/AssignRole.vue';
import ModuleManagement from '../components/ModuleManagement.vue';
import RoleForm from '../components/RoleForm.vue'; 

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login },
  {
    path: '/management',
    component: Management,
    children: [
      { path: 'dashboard', component: Dashboard },
      { path: 'user-management', component: UserManagement, name: 'userManagement' },
      { path: 'role-management', component: RoleManagement, name: 'roleManagement' },
      { path: 'pending_list', component: PendingList, name: 'pendingList' },
      { path: 'edit_user/:userId', component: EditUser, name: 'editUser' },
      { path: 'assign_role/:userId', component: AssignRole, name: 'assignRole' },
      { path: 'module-management', component: ModuleManagement, name: 'moduleManagement' },
      { path: 'create_role', component: RoleForm, name: 'createRole' }, // 新增角色的路由
      { path: 'edit_role/:roleId', component: RoleForm, name: 'editRole' }, // 编辑角色的路由
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
