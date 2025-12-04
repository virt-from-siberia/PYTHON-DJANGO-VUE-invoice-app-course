<template>
  <div class="page-login">
    <div class="columns">
      <div class="column is-4 is-offset-4">
        <h1 class="title">Log in</h1>

        <form @submit.prevent="submitForm">
          <div class="field">
            <label for="">Username</label>
            <div class="control">
              <input type="text" name="username" class="input" v-model="username">
            </div>
          </div>


          <div class="field">
            <label for="">Password</label>
            <div class="control">
              <input type="password" name="password" class="input" v-model="password">
            </div>
          </div>


          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">
              {{ error }}
            </p>
          </div>


          <div class="field">
            <div class="control">
              <button class="button is-success" :class="{ 'is-loading': isLoading }" :disabled="isLoading">
                Sign up
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'LogIn'
}
</script>
