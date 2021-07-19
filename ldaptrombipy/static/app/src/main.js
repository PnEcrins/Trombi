import { createApp } from 'vue'
import App from './App.vue'
import axios from "axios"
// load config
axios.get(`${process.env.BASE_URL}/config.json`).then(resp => {
    const app = createApp(App)
    app.config.globalProperties.$config = resp.data
    app.mount('#app')
})

