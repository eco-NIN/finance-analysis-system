<!-- @Author  : eco
     @Date    : 2025/6/7
     @Function: 东方财富数据爬取预测页面 -->
<template>
  <div class="page-container">
    <el-container>
      <el-header style="text-align: center">
        <h2>东方财富数据爬取与预测</h2>
      </el-header>

      <el-main>
        <el-form :inline="true" @submit.prevent>
          <el-form-item label="股票代码">
            <el-input v-model="form.stock_code" placeholder="如 600519" />
          </el-form-item>
          <el-form-item label="数据类型">
            <el-select v-model="form.data_type" placeholder="请选择" style="width: 100px;">
              <el-option label="行情" value="行情" />
              <el-option label="财报" value="财报" />
              <el-option label="新闻" value="新闻" />
            </el-select>
          </el-form-item>
          <el-form-item label="预测算法">
            <el-select v-model="form.algorithm" placeholder="请选择" style="width: 100px;">
<!--              线性回归-->
<!--              随机森林-->
<!--              逻辑回归-->
<!--              支持向量机-->
              <el-option label="线性回归" value="回归" />
              <el-option label="随机森林" value="随机森林" />

              <el-option label="逻辑回归" value="逻辑回归" />
              <el-option label="支持向量机" value="支持向量机" />
            </el-select>
          </el-form-item>
          <el-button type="primary" @click="fetchPrediction">开始预测</el-button>
        </el-form>

        <el-divider />

        <el-card v-if="prediction.length" class="card">
          <h3>预测结果</h3>
          <el-table :data="predictionTable" style="width: 100%">
            <el-table-column prop="day" label="预测日" />
            <el-table-column prop="value" label="预测值" />
          </el-table>
          <p>均方误差 (MSE)：{{ metrics.mse.toFixed(2) }}</p>
        </el-card>

        <el-card v-if="rawData.length" class="card">
          <h3>原始数据(展示前10条)</h3>
          <el-table :data="rawData.slice(0,10)" style="width: 100%">
            <el-table-column prop="date" label="日期" />
            <el-table-column prop="open" label="开盘价" />
            <el-table-column prop="close" label="收盘价" />
            <el-table-column prop="high" label="最高价" />
            <el-table-column prop="low" label="最低价" />
            <el-table-column prop="volume" label="成交量" />
            <el-table-column prop="amount" label="成交额" />
            <el-table-column prop="amplitude" label="振幅" />
            <el-table-column prop="change_pct" label="涨跌幅(%)" />
            <el-table-column prop="change_amt" label="涨跌额" />
            <el-table-column prop="turnover" label="换手率(%)" />
          </el-table>
        </el-card>
        <el-card v-if="cleanedData.length" class="card">
          <h3>清洗后的数据（前10条）</h3>
          <el-table :data="cleanedData.slice(0,10)" style="width: 100%">
            <el-table-column prop="date" label="日期" />
            <el-table-column prop="open" label="开盘价" />
            <el-table-column prop="close" label="收盘价" />
            <el-table-column prop="change_pct" label="涨跌幅(%)" />
          </el-table>
        </el-card>


      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import {reactive, ref} from 'vue'
import axios from 'axios'
// import { fetchPrediction } from '../services/Dongfang.js'


const form = ref({
  stock_code: '600519',
  data_type: '',
  algorithm: '',
})

const rawData = ref([])
const cleanedData = ref([])
const prediction = ref([])
const metrics = ref({ mse: 0 })

const predictionTable = ref([])

const fetchPrediction = async () => {
  try {
    const res = await axios.post('http://127.0.0.1:8000/api/v1/prediction/predict', {
      stock_code: form.value.stock_code,
      data_type: form.value.data_type,
      algorithm: form.value.algorithm
    })
    const data = res.data

    // 假设后端返回包含以下字段
    rawData.value = data.raw_data || []
    cleanedData.value = data.clean_data || []
    prediction.value = data.prediction || []
    metrics.value = data.metrics || {}

    // 构造表格用数据
    predictionTable.value = prediction.value.map((val, index) => ({
      day: `第${index + 1}天`,
      value: val.toFixed(2)
    }))
  } catch (err) {
    console.error(err)
  }
}
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
.card {
  margin-top: 20px;
}
</style>