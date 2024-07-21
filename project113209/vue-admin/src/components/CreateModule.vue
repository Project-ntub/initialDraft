<template>
    <div class="container">
      <form @submit.prevent="createModule">
        <div class="form-group">
          <label for="module_name">模組名稱</label>
          <input type="text" v-model="moduleName" id="module_name" required />
        </div>
        <button type="submit" class="btn">新增模組</button>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "CreateModule",
    data() {
      return {
        moduleName: ""
      };
    },
    methods: {
      createModule() {
        // 發送請求到後端
        this.$http.post("/backend/create_module", { module_name: this.moduleName })
          .then(response => {
            if (response.data.success) {
              this.$router.push({ name: 'moduleManagement' });
            } else {
              alert("新增模組失敗");
            }
          });
      }
    }
  };
  </script>
  
  <style scoped src="../assets/css/CreateModule.css"></style>

  