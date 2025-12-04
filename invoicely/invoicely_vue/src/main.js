import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import axios from "axios";

// В режиме разработки используем прокси из vue.config.js (относительные пути)
// В продакшене можно установить полный URL
if (process.env.NODE_ENV === 'production') {
  axios.defaults.baseURL = "http://127.0.0.1:8000";
}

createApp(App).use(store).use(router, axios).mount("#app");
