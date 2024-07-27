<template>
  <div class="container">
    <h2>{{ isEdit ? "編輯模組" : "新增模組" }}</h2>
    <form @submit.prevent="saveModule">
      <div class="form-group">
        <label for="module-name">模組名稱</label>
        <input type="text" v-model="localModule.name" id="module-name" required />
      </div>
      <button type="submit" class="btn">{{ isEdit ? "保存變更" : "新增" }}</button>
      <button type="button" class="btn secondary" @click="cancel">取消</button>
    </form>
  </div>
</template>

<script>
import axios from '../axios';

export default {
  name: "ModuleForm",
  data() {
    return {
      localModule: {
        name: '',
        is_deleted: false
      },
      isEdit: false
    };
  },
  methods: {
    async saveModule() {
      try {
        const response = await axios.post('/api/backend/modules/', { name: this.localModule.name });
        if (response.status === 201) {
          alert('保存成功');
          this.$emit('close');
        } else {
          alert('保存失敗');
        }
      } catch (error) {
        console.error('Error saving module:', error.response ? error.response.data : error.message);
        alert('保存失敗');
      }
    },
    cancel() {
      this.$emit('close');
    }
  },
  async mounted() {
    const moduleId = this.$route.params.moduleId;
    if (moduleId) {
      this.isEdit = true;
      await this.loadModule(moduleId);
    }
  }
};
</script>

<style scoped src="../assets/css/CreateModule.css"></style>
