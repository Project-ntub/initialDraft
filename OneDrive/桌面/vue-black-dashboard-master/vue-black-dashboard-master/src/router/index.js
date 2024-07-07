// router/index.js

import Vue from "vue";
import VueRouter from "vue-router";
import routes from "./routes";

Vue.use(VueRouter);

const router = new VueRouter({
  routes,
  linkExactActiveClass: "active",
  scrollBehavior: (to) => {
    if (to.hash) {
      return { selector: to.hash };
    } else {
      return { x: 0, y: 0 };
    }
  },
});

// 全域導航守衛
// router.beforeEach((to, from, next) => {
//   const isAuthenticated = false; // 假設使用者未驗證
//   // if (to.path !== "/login" && !isAuthenticated) {
//     next("/login"); // 導向登入頁面
//   } else {
//     next(); // 允許正常導航到其他路由
//   }
// });

export default router;
