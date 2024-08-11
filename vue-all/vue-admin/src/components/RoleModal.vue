<template>
  <div v-if="isVisible" class="modal-overlay">
    <div class="modal">
      <button class="close-btn" @click="$emit('close')">X</button>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  name: "RoleModal",
  props: {
    isVisible: {
      type: Boolean,
      required: true
    }
  }
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  max-width: 500px;
  width: 100%;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.close-btn {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
}
</style>
