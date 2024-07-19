<template>
  <div class="personal-card">
    <img :src="userData?.avatar || 'https://via.placeholder.com/150'" alt="Avatar">
    <h2>{{ userData?.name }}</h2>
    <h3>{{ userData?.position }}</h3>
    <p>{{ userData?.department }}</p>
    <p>{{ userData?.email }}</p>
    <p>{{ userData?.phone }}</p>
    <button class="edit-button" @click="$emit('edit')">編輯</button>
  </div>
</template>

<script>
export default {
  name: 'PersonalCard',
  props: {
    userData: {
      type: Object,
      required: true,
      default: () => ({
        avatar: '',
        name: '',
        position: '',
        department: '',
        email: '',
        phone: ''
      })
    }
  }
};
</script>

<style scoped>
.personal-card {
  background-color: #2c3e50;
  color: white;
  text-align: center;
  padding: 20px;
  border-radius: 10px;
  width: 100%;
  max-width: 400px;
}

.personal-card img {
  border-radius: 50%;
  width: 150px;
  height: 150px;
  margin-bottom: 20px;
}

.personal-card h2 {
  font-size: 1.5rem; /* 调整标题字体大小 */
}

.personal-card h3 {
  font-size: 1.2rem; /* 调整副标题字体大小 */
}

.personal-card p {
  font-size: 1rem; /* 调整段落字体大小 */
}

.edit-button {
  padding: 10px 20px;
  background-color: #6200ea;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

.edit-button:hover {
  background-color: #3700b3;
}
</style>
