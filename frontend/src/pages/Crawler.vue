<!--
@Author  : eco
@Date    :2025/5/22 11:06
@Function: 
-->

<!-- frontend/src/pages/Crawler.vue -->





<!--<template>-->
<!--  <div>-->
<!--    <h2>🕸️ 数据爬虫页面</h2>-->



<!--    <el-button type="primary" @click="fetchStockData" :loading="loading">-->
<!--      抓取基础股票数据-->
<!--    </el-button>-->

<!--    <div v-if="message" style="margin-top: 20px;">-->
<!--      <el-alert :title="message" type="success" show-icon />-->
<!--    </div>-->

<!--    <el-table-->
<!--      v-if="stockList.length"-->
<!--      :data="stockList"-->
<!--      style="width: 100%; margin-top: 20px"-->
<!--      stripe-->
<!--      border-->
<!--    >-->
<!--      <el-table-column prop="ts_code" label="股票代码" width="150" />-->
<!--      <el-table-column prop="name" label="股票名称" width="150" />-->
<!--      <el-table-column prop="area" label="地区" width="150" />-->
<!--      <el-table-column prop="industry" label="所属行业" />-->
<!--      <el-table-column prop="market" label="市场" />-->
<!--    </el-table>-->

<!--  </div>-->
<!--</template>-->

<!--<script setup>-->
<!--import { ref } from 'vue'-->
<!--import { ElMessage } from 'element-plus'-->
<!--import { fetchStockBasic } from '../services/crawler'-->

<!--const loading = ref(false)-->
<!--const message = ref('')-->
<!--const stockList = ref([])-->

<!--const fetchStockData = async () => {-->
<!--  loading.value = true-->
<!--  try {-->
<!--    const res = await fetchStockBasic()-->
<!--    message.value = res.message-->
<!--    stockList.value = res.data || []-->
<!--    ElMessage.success('抓取成功！')-->
<!--  } catch (error) {-->
<!--    ElMessage.error('抓取失败，请检查后端服务或网络')-->
<!--  } finally {-->
<!--    loading.value = false-->
<!--  }-->
<!--}-->

<!--</script>-->



<template>
  <div>
    <h2>🕸️ 数据爬虫</h2>
    <el-button @click="fetchStockData" type="primary" :loading="fetchLoading">
      抓取最新数据
    </el-button>

    <el-button @click="loadStockList" type="warning" :loading="listLoading">
      从数据库加载股票基础信息
    </el-button>

    <p>{{ message }}</p>
<!--    <div style="margin: 10px 0;">-->
<!--      <button @click="handleFetch" style="margin-right: 10px;">📥 一键抓取并存库</button>-->
<!--      <button @click="getStockList">🔄 仅从数据库加载</button>-->
<!--    </div>-->

<!--    <p v-if="message">{{ message }}</p>-->

    <el-table :data="stockList" style="width: 100%; margin-top: 20px;">
      <el-table-column prop="ts_code" label="股票(TS)代码" width="150" />
      <el-table-column prop="name" label="股票名称" width="150" />
      <el-table-column prop="area" label="地区" width="150" />
      <el-table-column prop="industry" label="所属行业" />
      <el-table-column prop="market" label="市场" />
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchStockBasic, getStockList } from '../services/crawler'
import { ElMessage } from 'element-plus'

const fetchLoading = ref(false)
const listLoading = ref(false)

const message = ref('')
const stockList = ref([])

const loadStockList = async () => {
  listLoading.value = true
  try {
    const res = await getStockList()
    stockList.value = res.data || []
  } catch (err) {
    ElMessage.error('获取数据失败')
  } finally {
    listLoading.value = false
  }
}

const fetchStockData = async () => {
  fetchLoading.value = true
  try {
    const res = await fetchStockBasic()
    message.value = res.message
    ElMessage.success('抓取成功')
    await loadStockList()
  } catch (err) {
    ElMessage.error('抓取失败，请检查后端服务或网络')
  } finally {
    fetchLoading.value = false
  }
}

// onMounted(() => {
//   loadStockList()
// })
</script>