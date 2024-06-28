import Notifications from "./Notifications.vue";

// 定義通知存儲對象
const NotificationStore = {
  state: [], // 存放通知的數組
  settings: { // 預設設置
    overlap: false, // 是否允許通知重疊
    verticalAlign: "top", // 垂直對齊方式
    horizontalAlign: "right", // 水平對齊方式
    type: "info", // 默認通知類型
    timeout: 5000, // 默認通知消失時間（毫秒）
    closeOnClick: true, // 是否點擊後關閉通知
    showClose: true, // 是否顯示關閉按鈕
  },
  // 設置選項，合併用戶設置和預設設置
  setOptions(options) {
    this.settings = Object.assign(this.settings, options);
  },
  // 移除指定時間戳的通知
  removeNotification(timestamp) {
    const indexToDelete = this.state.findIndex(
      (n) => n.timestamp === timestamp
    );
    if (indexToDelete !== -1) {
      this.state.splice(indexToDelete, 1);
    }
  },
  // 添加通知到 state 中
  addNotification(notification) {
    // 如果通知是字符串，轉換為對象
    if (typeof notification === "string" || notification instanceof String) {
      notification = { message: notification };
    }
    // 為通知添加時間戳
    notification.timestamp = new Date();
    notification.timestamp.setMilliseconds(
      notification.timestamp.getMilliseconds() + this.state.length
    );
    // 合併通知設置和預設設置
    notification = Object.assign({}, this.settings, notification);
    // 將通知添加到 state 中
    this.state.push(notification);
  },
  // 通知函數，支持批量通知
  notify(notification) {
    if (Array.isArray(notification)) {
      notification.forEach((notificationInstance) => {
        this.addNotification(notificationInstance);
      });
    } else {
      this.addNotification(notification);
    }
  },
};

// 定義通知插件
const NotificationsPlugin = {
  install(Vue, options) {
    // 創建一個 Vue 實例來管理通知存儲
    let app = new Vue({
      data: {
        notificationStore: NotificationStore,
      },
      methods: {
        notify(notification) {
          this.notificationStore.notify(notification);
        },
      },
    });
    // 添加通知方法到 Vue 原型
    Vue.prototype.$notify = app.notify;
    // 添加通知存儲到 Vue 原型
    Vue.prototype.$notifications = app.notificationStore;
    // 全局註冊 Notifications 組件
    Vue.component("Notifications", Notifications);
    // 設置插件選項
    if (options) {
      NotificationStore.setOptions(options);
    }
  },
};

export default NotificationsPlugin;
