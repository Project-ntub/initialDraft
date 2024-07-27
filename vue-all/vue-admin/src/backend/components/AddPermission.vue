<template>
    <div class="container">
      <h2>新增權限</h2>
      <form @submit.prevent="addPermission">
        <table class="permission-table">
          <thead>
            <tr>
              <th>功能</th>
              <th>新增</th>
              <th>查詢</th>
              <th>檢視</th>
              <th>修改</th>
              <th>刪除</th>
              <th>列印</th>
              <th>匯出</th>
              <th>維護</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><input type="text" v-model="permissionName" required /></td>
              <td><input type="checkbox" v-model="canAdd" /></td>
              <td><input type="checkbox" v-model="canQuery" /></td>
              <td><input type="checkbox" v-model="canView" /></td>
              <td><input type="checkbox" v-model="canEdit" /></td>
              <td><input type="checkbox" v-model="canDelete" /></td>
              <td><input type="checkbox" v-model="canPrint" /></td>
              <td><input type="checkbox" v-model="canExport" /></td>
              <td><input type="checkbox" v-model="canMaintain" /></td>
            </tr>
          </tbody>
        </table>
        <div class="button-group">
          <button type="submit" class="btn">新增</button>
          <button type="button" class="btn secondary" @click="cancel">取消</button>
        </div>
      </form>
    </div>
  </template>
  
  <script>
  export default {
    name: "AddPermission",
    data() {
      return {
        permissionName: "",
        canAdd: false,
        canQuery: false,
        canView: false,
        canEdit: false,
        canDelete: false,
        canPrint: false,
        canExport: false,
        canMaintain: false
      };
    },
    methods: {
      addPermission() {
        // 發送請求到後端
        this.$http.post("/backend/add_permission", {
          permission_name: this.permissionName,
          can_add: this.canAdd,
          can_query: this.canQuery,
          can_view: this.canView,
          can_edit: this.canEdit,
          can_delete: this.canDelete,
          can_print: this.canPrint,
          can_export: this.canExport,
          can_maintain: this.canMaintain
        }).then(response => {
          if (response.data.success) {
            alert("新增成功");
          } else {
            alert("新增失敗");
          }
        });
      },
      cancel() {
        this.$router.go(-1);
      }
    }
  };
  </script>
  
  <style scoped src="../assets/css/AddPermission.css"></style>
