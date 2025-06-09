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
            <el-input v-model="form.stock_code" placeholder="如 600519" style="width: 100px;" />
          </el-form-item>
          <el-form-item label="数据类型">
            <el-select v-model="form.data_type" placeholder="请选择" style="width: 100px;">
              <el-option label="行情" value="行情" />
              <el-option label="财报" value="财报" />
              <el-option label="新闻" value="新闻" />
            </el-select>
          </el-form-item>

          <el-form-item label="任务类型">
            <el-radio-group v-model="form.task_type">
              <el-radio-button label="回归">回归任务</el-radio-button>
              <el-radio-button label="分类">分类任务</el-radio-button>
            </el-radio-group>
          </el-form-item>

          <el-form-item label="预测算法" style="width: 200px;">
            <el-select v-model="form.algorithm" :disabled="!form.task_type">
              <!-- 动态显示算法选项 -->
              <el-option
                v-if="form.task_type === '回归'"
                v-for="item in regressionAlgorithms"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
              <el-option
                v-if="form.task_type === '分类'"
                v-for="item in classificationAlgorithms"
                :key="item.value"
                :label="item.label"
                :value="item.value"
              />
            </el-select>
          </el-form-item>
          <el-form-item label="时间范围">
            <el-date-picker
              v-model="dateRange"
              type="daterange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              value-format="YYYYMMDD"
            />
          </el-form-item>
          <el-button type="primary" @click="fetchPrediction">开始预测</el-button>
        </el-form>

        <el-divider />

          <el-card v-if="prediction.length">
            <h3>结束日期未来几天预测结果（{{ form.task_type }} - {{ form.algorithm }}）</h3>

            <!-- 回归任务显示数值 -->
            <el-table v-if="form.task_type === '回归'" :data="predictionTable">
              <el-table-column prop="day" label="预测日" />
              <el-table-column prop="value" label="收盘价预测" />
            </el-table>

            <!-- 分类任务显示涨跌 -->
            <el-table v-else :data="predictionTable">
              <el-table-column prop="day" label="预测日" />
              <el-table-column prop="value" label="涨跌预测">
                <template #default="{ row }">
                  <el-tag :type="row.value === 1 ? 'success' : 'danger'">
                    {{ row.value === 1 ? '上涨' : '下跌' }}
                  </el-tag>
                </template>
              </el-table-column>
            </el-table>

            <!-- 动态显示评估指标 -->
            <p v-if="form.task_type === '回归'">
              均方误差 (MSE)：{{ metrics.mse?.toFixed(4) || 'N/A' }}
            </p>
            <p v-else>
              准确率 (Accuracy)：{{ (metrics.accuracy * 100)?.toFixed(2) || 'N/A' }}%
            </p>
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

        <el-card v-if="cleanedData.length">
          <h3>清洗后的数据（含技术指标）</h3>
          <el-table :data="cleanedData.slice(0, 10)">
            <el-table-column prop="date" label="日期" width="100" />
            <el-table-column prop="open" label="开盘价" width="90" />
            <el-table-column prop="close" label="收盘价" width="90" />
            <el-table-column prop="high" label="最高价" width="90" />
            <el-table-column prop="low" label="最低价" width="90" />
            <el-table-column prop="volume" label="成交量" width="80" />
            <el-table-column prop="change_pct" label="涨跌幅(%)" width="130" />
            <el-table-column prop="ma_5" label="5日均线" width="100" />
            <el-table-column prop="ma_10" label="10日均线" width="170" />
            <el-table-column prop="volatility" label="波动率" width="170" />
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

//value是后端接受的值
const regressionAlgorithms = [
  { label: '线性回归', value: '线性回归' },
  { label: '随机森林回归', value: '随机森林' }
]

const classificationAlgorithms = [
  { label: '逻辑回归', value: '逻辑回归' },
  { label: '支持向量机', value: '支持向量机' }
]
const dateRange = ref([]) // 存储日期范围
const form = ref({
  stock_code: '600519',
  data_type: '行情',
  task_type: '', // 新增：回归/分类
  algorithm: ''  // 根据任务类型动态填充
})

const rawData = ref([])
const cleanedData = ref([])
const prediction = ref([])
const metrics = ref({ mse: 0 })
const predictionTable = ref([])

const fetchPrediction = async () => {
  try {
    const [startDate, endDate] = dateRange.value || []
    const res = await axios.post('/api/v1/prediction/predict', {
      stock_code: form.value.stock_code,
      data_type: form.value.data_type,
      task_type: form.value.task_type, // 新增
      algorithm: form.value.algorithm,
      start_date: startDate,  // 传递日期参数
      end_date: endDate
    })
    // 类型转换处理
    const predictionNumbers = res.data.prediction.map(Number); // 字符串转数字
    // 处理结果（保持不变）
    rawData.value = res.data.raw_data || []
    cleanedData.value = res.data.clean_data || []
    prediction.value = predictionNumbers; // 使用转换后的数值数组
    metrics.value = res.data.metrics || {}
    // 动态构造预测表格
    predictionTable.value = res.data.prediction.map((val, i) => ({
      day: `第${i+1}天`,
      value: form.value.task_type === '回归' ?
        val.toFixed(2) :  // 回归任务：数值格式化
        (val === 1 ? '上涨' : '下跌')  // 分类任务：转为文字
    }))

  } catch (err) {
    ElMessage.error(`预测失败: ${err.response?.data?.detail || err.message}`)
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
