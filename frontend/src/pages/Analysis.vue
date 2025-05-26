<template>
  <div style="padding: 20px">
    <h2>🏦金融分析页面</h2>

    <el-form :model="form" label-width="100px" style="max-width: 500px">
      <el-form-item label="股票代码">
        <el-input v-model="form.stock_code" placeholder="如：600519.SH" />
      </el-form-item>
      <el-form-item label="开始日期">
        <el-date-picker v-model="form.start_date" type="date" placeholder="选择开始日期" format="YYYY-MM-DD" />
      </el-form-item>
      <el-form-item label="结束日期">
        <el-date-picker v-model="form.end_date" type="date" placeholder="选择结束日期" format="YYYY-MM-DD" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onAnalyze">开始分析</el-button>
      </el-form-item>
    </el-form>

    <div v-if="resultData" style="margin-top: 30px">
      <h3>📊 分析结果：</h3>
      <el-card>
        <p>平均收盘价：{{ resultData.average_close }}</p>
        <p>最高收盘价：{{ resultData.max_close }}</p>
        <p>最低收盘价：{{ resultData.min_close }}</p>
      </el-card>
    </div>

    <div v-if="imageUrl" style="margin-top: 20px">
      <h3>📈 收盘价趋势图：</h3>
      <img :src="imageUrl" alt="分析图表" style="max-width: 100%" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { ElMessage } from 'element-plus'
import { fetchAnalysisResults } from '../analysis'

const form = ref({
  stock_code: '600519.SH',  // 默认示例代码
  start_date: '2024-01-01',
  end_date: '2024-12-31',
})

const resultData = ref(null)
const imageUrl = ref('')

const onAnalyze = async () => {
  try {
    const res = await fetchAnalysisResults(form.value)
    resultData.value = res.data.result
    imageUrl.value = `data:image/png;base64,${res.data.image_base64}`
    ElMessage.success('分析完成')
  } catch (err) {
    console.error(err)
    ElMessage.error('分析失败，请检查输入或后端服务')
  }
}
</script>

<style scoped>
h2 {
  font-weight: bold;
}
</style>
