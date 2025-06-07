// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Crawler from '../pages/Crawler.vue'
import Analysis from '../pages/Analysis.vue'
import Prediction from '../pages/Prediction.vue'
import History from '../pages/History.vue'
import Dongfang from "../pages/Dongfang.vue";

const routes = [
  { path: '/', component: Home },
  { path: '/crawler', component: Crawler },
  { path: '/analysis', component: Analysis },
  { path: '/prediction', component: Prediction },
  { path: '/history', component: History },
  { path: '/dongfang', component: Dongfang}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router