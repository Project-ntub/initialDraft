<!-- eslint-disable vue/no-mutating-props -->
<template>
  <card>
    <h5 slot="header" class="title">編輯個人資訊</h5>
    <div class="row">
      <!-- <div class="col-md-5 pr-md-1">
        <base-input
          label="Company (disabled)"
          placeholder="Company"
          v-model="model.company"
          disabled
        >
        </base-input>
      </div> -->
      <div class="col-md-3 px-md-1">
        <base-input
          label="帳號"
          placeholder="帳號"
          v-model="model.username"
        >
        </base-input>
      </div>
      <div class="col-md-6 pl-md-1">
        <base-input
          label="電子郵件"
          type="email"
          placeholder="電子郵件"
        >
        </base-input>
      </div>
    </div>
    <div class="row">
      <div class="col-md-4 pr-md-1">
        <base-input
          label="姓名"
          v-model="model.name"
          placeholder="姓名"
        >
        </base-input>
      </div>
      <div class="col-md-6 pl-md-1">
        <base-input
          label="部門"
          v-model="model.department"
          placeholder="部門"
        >
        </base-input>
        <div class="col-md-6 pr-md-1">
        <base-input
          label="職位"
          v-model="model.position"
          placeholder="職位"
        ></base-input>
      </div>
      <div class="col-md-6 pl-md-1">
        <base-input
          label="電話"
          type="tel"
          v-model="model.phone"
          placeholder="電話"
        ></base-input>
      </div>
    </div>
    <div class="row">
      <!-- <div class="col-md-6 pr-md-1">
        <base-input
          label="建立時間"
          type="datetime-local"
          v-model="model.creationTime"
          placeholder="建立時間"
        ></base-input>
      </div> -->
      </div>
    </div>
    <div class="row">
      
      <!-- <div class="col-md-12">
        <base-input
          label="Address"
          v-model="model.address"
          placeholder="Home Address"
        >
        </base-input>
      </div> -->
    </div>
    <!-- <div class="row">
      <div class="col-md-4 pr-md-1">
        <base-input label="City" v-model="model.city" placeholder="City">
        </base-input>
      </div>
      <div class="col-md-4 px-md-1">
        <base-input
          label="Country"
          v-model="model.country"
          placeholder="Country"
        >
        </base-input>
      </div>
      <div class="col-md-4 pl-md-1">
        <base-input label="Postal Code" placeholder="ZIP Code"> </base-input>
      </div>
    </div> -->
    <!-- <div class="row">
      <div class="col-md-8">
        <base-input>
          <label>About Me</label>
          <textarea
            rows="4"
            cols="80"
            class="form-control"
            placeholder="Here can be your description"
            v-model="model.about"
          >
          </textarea>
        </base-input>
      </div>
    </div> -->
    <base-button slot="footer" type="primary" fill>儲存</base-button>
    <base-button slot="footer" type="primary" fill>取消</base-button>
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
<style></style>
