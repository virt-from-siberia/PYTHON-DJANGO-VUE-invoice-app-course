<template>
  <div class="page-my-account">
    <h1 class="title">My account</h1>
    <button @click="logout()" class="button is-danger">Log out</button>
  </div>
</template>

<script>
import axios from 'axios'
import { handleApiError } from '@/utils/errorHandler'

export default {
  name: "MyAccount",
  data() {
    return {
      errors: []
    }
  },
  methods: {
    logout() {
      axios.post('/api/v1/token/logout').then(response => {
        axios.defaults.headers.common["Authorization"] = ""

        localStorage.removeItem("token")

        this.$store.commit('removeToken')

        this.$router.push('/')
      }).catch(error => {
        handleApiError(error, this.errors)
      })
    }
  }
}

</script>
