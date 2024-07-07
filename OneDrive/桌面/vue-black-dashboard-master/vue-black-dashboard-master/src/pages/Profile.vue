<template>
  <div class="row">
    <div class="col-md-8">
      <edit-profile-form :model="model"> </edit-profile-form>
    </div>
  </div>
</template>
<script>
import EditProfileForm from "./Profile/EditProfileForm";
export default {
  components: {
    EditProfileForm,
  },
  data() {
    return {
      model: {
        company: "Creative Code Inc.",
        email: "mike@email.com",
        username: "michael23",
        // address: "Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09",
        city: "Melbourne",
        country: "Australia",
        
      },
      user: {
        fullName: "Mike Andrew",
        title: "Ceo/Co-Founder",
        description: `Do not be scared of the truth because we need to restart the human foundation in truth And I love you like Kanye loves Kanye I love Rick Owens’ bed design but the back is...`,
      },
    };
  },
};
</script>
<style></style>
