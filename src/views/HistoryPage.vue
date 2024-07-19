<template>
  <div class="history-page">
    <div class="container">
      <div class="search-container">
        <input type="text" id="searchInput" placeholder="搜尋紀錄..." v-model="searchQuery">
        <button @click="filterTimeline">搜尋</button>
      </div>
      <ul class="timeline" id="timeline">
        <li class="timeline-item" v-for="item in filteredItems" :key="item.id" @click="showDetail(item.id)">
          <div class="timeline-panel">
            <div class="timeline-heading">
              <h4>{{ item.date }}</h4>
            </div>
            <div class="timeline-body">
              <p>{{ item.action }}</p>
              <div class="timeline-user">使用者: {{ item.user }}</div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HistoryPage',
  data() {
    return {
      searchQuery: '',
      items: [
        { id: 1, date: '2024/1/22 16:22:39', action: '編輯個人資訊', user: 'User1' },
        { id: 2, date: '2024/1/22 16:00:21', action: '查看首頁', user: 'User2' },
        { id: 3, date: '2024/1/28 16:00:21', action: '修改密碼', user: 'User2' },
        { id: 4, date: '2023/12/28 16:00:21', action: '忘記密碼', user: 'User2' },
        // 添加更多的歷史紀錄項目
      ]
    }
  },
  computed: {
    filteredItems() {
      return this.items.filter(item => {
        const query = this.searchQuery.trim().toUpperCase();
        return item.action.toUpperCase().includes(query) || item.date.includes(query);
      });
    }
  },
  methods: {
    filterTimeline() {
      // 使用计算属性进行过滤，不需要额外的过滤逻辑
    },
    showDetail(id) {
      this.$router.push(`/detail/${id}`);
    },
    logout() {
      alert("已登出");
      this.$router.push('/login');
    }
  }
}
</script>

<style scoped src="../assets/css/HistoryPage.css"></style>
