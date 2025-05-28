// frontend/src/main.js 加入 Element Plus
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

const app = createApp(App)
app.use(createPinia())
app.use(router)
app.use(ElementPlus)
app.mount('#app')


// 状态管理（Pinia）：保存分析页面的表单参数和结果，预测页面共享调用
const pinia = createPinia()
app.use(pinia)