<template>
  <div class="container">
    <h2>{{ moduleId ? '編輯模組' : '新增模組' }}</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="module-name">模組名稱</label>
        <input type="text" v-model="localModuleName" id="module-name" required />
      </div>
      <button type="submit" class="btn">{{ moduleId ? '保存變更' : '新增' }}</button>
      <button type="button" class="btn secondary" @click="close">取消</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "ModuleForm",
  props: {
    moduleId: {
      type: [String, Number],
      default: null
    },
    moduleName: {
      type: String,
      default: ""
    }
  },
  data() {
    return {
      localModuleName: this.moduleName
    };
  },
  methods: {
    close() {
      this.$emit('close');
    },
    handleSubmit() {
      const moduleData = { name: this.localModuleName };
      if (this.moduleId) {
        this.$emit('edit', moduleData);
      } else {
        this.$emit('create', moduleData);
      }
    }
  }
};
</script>

<style scoped src="../assets/css/ModuleForm.css"></style>
