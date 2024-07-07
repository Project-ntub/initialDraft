import DashboardLayout from "@/layout/dashboard/DashboardLayout.vue";
// GeneralViews
import NotFound from "@/pages/NotFoundPage.vue";
import Logout from '@/views/Logout.vue';
import Login from '@/pages/Login.vue';
import Register from '@/pages/Register.vue'; 
import ForgetPassword from '../pages/ForgetPassword.vue';
// Admin pages
const Dashboard = () =>
  import(/* webpackChunkName: "" */ "@/pages/Dashboard.vue");
const Profile = () =>
  import(/* webpackChunkName: "common" */ "@/pages/Profile.vue");
const Historyrecord = () =>
  import(/* webpackChunkName: "common" */ "@/pages/Historyrecord.vue");
const Accountsettings = () =>
  import(/* webpackChunkName: "common" */ "@/pages/Accountsettings.vue");
const Changepassword = () =>
  import(/* webpackChunkName: "common" */ "@/pages/Accountsettings/Changepassword.vue");
const Userpreference = () =>
  import(/* webpackChunkName: "common" */ "@/components/Preferences.vue");

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { layout: 'no-sidebar' }
  },
  {
    path: '/logout',
    name: 'Logout',
    component: Logout,
    meta: { layout: 'no-sidebar' }
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
    meta: { layout: 'no-sidebar' }
  },
  {
    path: '/forgetpassword',
    name: 'ForgetPassword',
    component: ForgetPassword
  },
  {
    path: "/",
    component: DashboardLayout,
    redirect: "/dashboard",
    children: [
      {
        path: "dashboard",
        name: "首頁",
        component: Dashboard,
      },
      {
        path: "profile",
        name: "個人資訊",
        component: Profile,
      },
      {
        path: "historyrecord",
        name: "歷史紀錄",
        component: Historyrecord,
      },
      {
        path: "accountsettings",
        name: "帳號設定",
        component: Accountsettings,
        children: [
          {
            path: "changepassword",
            name: "修改密碼",
            component: Changepassword,
          },
        ],
      },
      {
        path: "userpreferences",
        name: "偏好設定",
        component: Userpreference,
      },
     
      
    ],
  },
  { path: "*", component: NotFound },
];

export default routes;
