// src/router/index.js
import Vue from 'vue';
import Router from 'vue-router';
import Dashboard from '@/components/pages/Dashboard.vue';
import UserManagement from '@/components/pages/UserManagement.vue';
import RoleManagement from '@/components/pages/RoleManagement.vue';
import History from '@/components/pages/History.vue';
import Preferences from '@/components/pages/Preferences.vue';
import Profile from '@/components/pages/Profile.vue';
import LogoutSuccess from '@/components/pages/LogoutSuccess.vue';

Vue.use(Router);

export default new Router({
  routes: [
    { path: '/dashboard', component: Dashboard },
    { path: '/user-management', component: UserManagement },
    { path: '/role-management', component: RoleManagement },
    { path: '/history', component: History },
    { path: '/preferences', component: Preferences },
    { path: '/profile', component: Profile },
    { path: '/logout-success', component: LogoutSuccess },
    { path: '*', redirect: '/dashboard' }
  ]
});


