<template>
    <div id="app">
      <h1>個人偏好管理</h1>
      <form @submit.prevent="updatePreferences">
        <div class="form-group">
          <label for="font-size">字體大小:</label>
          <select id="font-size" v-model="preferences.font_size">
            <option value="small">小</option>
            <option value="medium">中</option>
            <option value="large">大</option>
          </select>
        </div>
        <div class="form-group">
          <label for="notifications">通知:</label>
          <input type="checkbox" id="notifications" v-model="preferences.notifications"> 啟用通知
        </div>
        <div class="form-group">
          <label for="auto-login">自動登入:</label>
          <input type="checkbox" id="auto-login" v-model="preferences.auto_login"> 啟用自動登入
        </div>
        <div class="form-group">
          <label for="verification">驗證:</label>
          <input type="checkbox" id="verification" v-model="preferences.verification"> 啟用驗證
        </div>
        <div class="btn-container">
          <button type="submit" class="btn">保存更改</button>
          <button type="button" class="btn" @click="showAddModal">新增</button>
          <button type="button" class="btn btn-delete" @click="deletePreference">刪除</button>
          <button type="button" class="btn btn-cancel" @click="resetPreferences">取消更改</button>
        </div>
      </form>
  
      <div v-if="successMessage" class="success-message">保存成功！</div>
  
      <div v-if="showModal" class="modal">
        <div class="modal-content">
          <span class="close" @click="closeAddModal">&times;</span>
          <h2>新增個人偏好</h2>
          <form @submit.prevent="addPreference">
            <div class="form-group">
              <label for="add-font-size">字體大小:</label>
              <select id="add-font-size" v-model="newPreference.font_size">
                <option value="small">小</option>
                <option value="medium">中</option>
                <option value="large">大</option>
              </select>
            </div>
            <div class="form-group">
              <label for="add-notifications">通知:</label>
              <input type="checkbox" id="add-notifications" v-model="newPreference.notifications"> 啟用通知
            </div>
            <div class="form-group">
              <label for="add-auto-login">自動登入:</label>
              <input type="checkbox" id="add-auto-login" v-model="newPreference.auto_login"> 啟用自動登入
            </div>
            <div class="form-group">
              <label for="add-verification">驗證:</label>
              <input type="checkbox" id="add-verification" v-model="newPreference.verification"> 啟用驗證
            </div>
            <div class="btn-container">
              <button type="submit" class="btn">保存</button>
              <button type="button" class="btn btn-cancel" @click="closeAddModal">取消</button>
            </div>
          </form>
        </div>
      </div>
  
      <h2>查詢個人偏好</h2>
      <form @submit.prevent="queryPreferences">
        <div class="form-group">
          <label for="query-font-size">字體大小:</label>
          <select id="query-font-size" v-model="query.font_size">
            <option value="">--選擇--</option>
            <option value="small">小</option>
            <option value="medium">中</option>
            <option value="large">大</option>
          </select>
        </div>
        <div class="form-group">
          <label for="query-notifications">通知:</label>
          <select id="query-notifications" v-model="query.notifications">
            <option value="">--選擇--</option>
            <option value="true">啟用</option>
            <option value="false">不啟用</option>
          </select>
        </div>
        <div class="form-group">
          <label for="query-auto-login">自動登入:</label>
          <select id="query-auto-login" v-model="query.auto_login">
            <option value="">--選擇--</option>
            <option value="true">啟用</option>
            <option value="false">不啟用</option>
          </select>
        </div>
        <div class="form-group">
          <label for="query-verification">驗證:</label>
          <select id="query-verification" v-model="query.verification">
            <option value="">--選擇--</option>
            <option value="true">啟用</option>
            <option value="false">不啟用</option>
          </select>
        </div>
        <div class="btn-container">
          <button type="submit" class="btn">查詢</button>
        </div>
      </form>
  
      <div class="results">
        <table v-if="queryResults.length">
          <thead>
            <tr>
              <th>ID</th>
              <th>字體大小</th>
              <th>通知</th>
              <th>自動登入</th>
              <th>驗證</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="result in queryResults" :key="result.id">
              <td>{{ result.id }}</td>
              <td>{{ result.font_size }}</td>
              <td>{{ result.notifications ? '啟用' : '不啟用' }}</td>
              <td>{{ result.auto_login ? '啟用' : '不啟用' }}</td>
              <td>{{ result.verification ? '啟用' : '不啟用' }}</td>
            </tr>
          </tbody>
        </table>
        <div v-else>沒有符合條件的偏好設置</div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        preferences: {
          font_size: 'medium',
          notifications: false,
          auto_login: false,
          verification: false
        },
        newPreference: {
          font_size: 'medium',
          notifications: false,
          auto_login: false,
          verification: false
        },
        query: {
          font_size: '',
          notifications: '',
          auto_login: '',
          verification: ''
        },
        queryResults: [],
        successMessage: false,
        showModal: false
      };
    },
    methods: {
      loadPreferences() {
        fetch('http://127.0.0.1:5000/get_preferences')
          .then(response => response.json())
          .then(data => {
            this.preferences = data;
          });
      },
      updatePreferences() {
        fetch('http://127.0.0.1:5000/update_preference', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.preferences)
        })
        .then(response => {
          if (response.ok) {
            this.successMessage = true;
            setTimeout(() => {
              this.successMessage = false;
            }, 3000);
          } else {
            alert('保存失敗');
          }
        });
      },
      showAddModal() {
        this.showModal = true;
      },
      closeAddModal() {
        this.showModal = false;
      },
      addPreference() {
        fetch('http://127.0.0.1:5000/add_preference', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.newPreference)
        })
        .then(response => {
          if (response.ok) {
            this.closeAddModal();
            this.successMessage = true;
            setTimeout(() => {
              this.successMessage = false;
            }, 3000);
          } else {
            alert('新增失敗');
          }
        });
      },
      deletePreference() {
        fetch('http://127.0.0.1:5000/delete_preference', {
          method: 'POST'
        })
        .then(response => {
          if (response.ok) {
            this.successMessage = true;
            setTimeout(() => {
              this.successMessage = false;
            }, 3000);
          } else {
            alert('刪除失敗');
          }
        });
      },
      resetPreferences() {
        this.loadPreferences();
      },
      queryPreferences() {
        let query = `http://127.0.0.1:5000/query_preferences?`;
        if (this.query.font_size) query += `font_size=${this.query.font_size}&`;
        if (this.query.notifications) query += `notifications=${this.query.notifications}&`;
        if (this.query.auto_login) query += `auto_login=${this.query.auto_login}&`;
        if (this.query.verification) query += `verification=${this.query.verification}&`;
        fetch(query.slice(0, -1))
          .then(response => response.json())
          .then(data => {
            this.queryResults = data;
          });
      }
    },
    mounted() {
      this.loadPreferences();
    }
  };
  </script>
  
  <style scoped>
  /* 在此處添加你的 CSS */
  </style>
  