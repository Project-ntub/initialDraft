<template>
  <card>
    <h5 slot="header" class="title">編輯個人資訊</h5>
    <div class="form-container">
      <div class="form-row">
        <div class="form-group">
          <base-input
            label="帳號"
            placeholder="帳號"
            v-model="model.username"
          ></base-input>
        </div>
        <div class="form-group">
          <base-input
            label="電子郵件"
            type="email"
            placeholder="電子郵件"
          ></base-input>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <base-input
            label="姓名"
            v-model="model.name"
            placeholder="姓名"
          ></base-input>
        </div>
        <div class="form-group">
          <base-input
            label="部門"
            v-model="model.department"
            placeholder="部門"
          ></base-input>
        </div>
      </div>
      <div class="form-row">
        <div class="form-group">
          <base-input
            label="職位"
            v-model="model.position"
            placeholder="職位"
          ></base-input>
        </div>
        <div class="form-group">
          <base-input
            label="電話"
            type="tel"
            v-model="model.phone"
            placeholder="電話"
          ></base-input>
        </div>
      </div>
    </div>
    <div class="form-actions">
      <base-button slot="footer" type="primary" fill>儲存</base-button>
      <base-button slot="footer" type="primary" fill>取消</base-button>
    </div>
  </card>
</template>

<script>
export default {
  props: {
    model: {
      type: Object,
      default: () => {
        return {};
      },
    },
  },
};
</script>

<style scoped>
.title {
  color: #fff;
}

.form-container {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-row {
  display: flex;
  gap: 16px;
}

.form-group {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.form-actions {
  display: flex;
  gap: 16px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #9c27b0;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #7b1fa2;
}
</style>
