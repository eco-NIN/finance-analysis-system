<!--
@Author  : eco
@Date    :2025/5/22 11:06
@Function: 
-->
<template>
  <div class="page-container">
      <div style="text-align: center;">
        <h2>🕸️ 股票基础信息（可用于分析）</h2>
          <div style="display: flex; justify-content: left; gap: 10px;">
            <el-button @click="fetchStockData" type="primary" :loading="fetchLoading">
              抓取最新股票信息
            </el-button>
            <el-button @click="loadStockList" type="warning" :loading="listLoading">
              从数据库加载股票基础信息
            </el-button>
          </div>

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

<style scoped>
/* 毛玻璃效果容器 */
.page-container {
  max-width: 1200px;
  margin: 20px auto;
  padding: 20px;
  background-color: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  border-radius: 15px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
</style>
