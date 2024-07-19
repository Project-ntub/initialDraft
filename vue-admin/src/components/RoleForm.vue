<template>
  <div class="container">
    <h2>{{ isEdit ? "編輯角色" : "新增角色" }}</h2>
    <form @submit.prevent="saveRole">
      <div class="form-group">
        <label for="role-name">角色名稱</label>
        <input type="text" v-model="localRole.name" id="role-name" required />
      </div>
      <div class="form-group">
        <label for="role-users">角色成員</label>
        <input type="text" v-model="localRole.users" id="role-users" />
      </div>
      <div class="form-group">
        <label for="role-is-active">角色狀態</label>
        <input type="checkbox" v-model="localRole.isActive" id="role-is-active" />
      </div>
      <div class="form-group">
        <label for="role-module">模組</label>
        <input type="text" v-model="localRole.module" id="role-module" />
      </div>
      <div v-if="isEdit" class="form-group">
        <label>角色權限</label>
        <table>
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
              <th>操作</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="permission in localRolePermissions" :key="permission.id">
              <td>{{ permission.permissionName }}</td>
              <td><input type="checkbox" v-model="permission.canAdd" /></td>
              <td><input type="checkbox" v-model="permission.canQuery" /></td>
              <td><input type="checkbox" v-model="permission.canView" /></td>
              <td><input type="checkbox" v-model="permission.canEdit" /></td>
              <td><input type="checkbox" v-model="permission.canDelete" /></td>
              <td><input type="checkbox" v-model="permission.canPrint" /></td>
              <td><input type="checkbox" v-model="permission.canExport" /></td>
              <td><input type="checkbox" v-model="permission.canMaintain" /></td>
              <td>
                <button type="button" @click="deletePermission(permission.id)">刪除</button>
              </td>
            </tr>
          </tbody>
        </table>
        <button type="button" @click="addPermission">新增權限</button>
      </div>
      <button type="submit" class="btn">{{ isEdit ? "保存變更" : "新增" }}</button>
      <button type="button" class="btn secondary" @click="cancel">取消</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "RoleForm",
  props: {
    isEdit: Boolean,
    role: Object,
    rolePermissions: Array
  },
  data() {
    return {
      localRole: { ...this.role },
      localRolePermissions: [ ...this.rolePermissions ]
    };
  },
  methods: {
    saveRole() {
      // 發送請求到後端
      this.$http.post("/backend/role_form", {
        role: this.localRole,
        role_permissions: this.localRolePermissions
      }).then(response => {
        if (response.data.success) {
          alert("保存成功");
        } else {
          alert("保存失敗");
        }
      });
    },
    deletePermission(permissionId) {
      // 刪除權限的邏輯
      this.localRolePermissions = this.localRolePermissions.filter(p => p.id !== permissionId);
    },
    addPermission() {
      // 新增權限的邏輯
      this.$router.push({ name: 'addPermission', params: { roleId: this.localRole.id } });
    },
    cancel() {
      this.$router.go(-1);
    }
  }
};
</script>

<style scoped src="../assets/css/RoleForm.css"></style>
