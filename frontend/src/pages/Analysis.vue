<template>
  <div class="page-container">
    <div class="header-container">
      <h2 class="page-title">🏦 金融分析页面</h2>
    </div>

    <el-form :model="form" label-width="100px" class="form-container">
      <el-form-item label="股票代码">
        <el-input v-model="form.ts_code" placeholder="如：600519.SH" style="width: 300px;" />
      </el-form-item>
      <el-form-item label="开始日期">
        <el-date-picker v-model="form.start_date" type="date" placeholder="选择开始日期" format="YYYY-MM-DD" style="width: 300px;" />
      </el-form-item>
      <el-form-item label="结束日期">
        <el-date-picker v-model="form.end_date" type="date" placeholder="选择结束日期" format="YYYY-MM-DD" style="width: 300px;" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onAnalyze" :loading="isLoading">开始分析</el-button>
      </el-form-item>
    </el-form>

    <div v-if="resultData" class="result-container">
      <el-card class="result-card">
        <h3 class="section-title">📊 分析结果：</h3>
        <div class="result-grid">
          <!-- 价格相关 -->
          <div class="result-block price-block">
            <h4 class="block-title price-title">价格相关</h4>
            <div class="result-item">
              <span class="result-label">平均收盘价：</span>
              <span class="result-value">{{ resultData.average_close.toFixed(2) }}</span>
            </div>
            <div class="result-item">
              <span class="result-label">最高收盘价：</span>
              <span class="result-value">{{ resultData.max_close.toFixed(2) }}</span>
            </div>
            <div class="result-item">
              <span class="result-label">最低收盘价：</span>
              <span class="result-value">{{ resultData.min_close.toFixed(2) }}</span>
            </div>
            <div class="result-item">
              <span class="result-label">波动率：</span>
              <span class="result-value">{{ (resultData.volatility * 100).toFixed(2) }}%</span>
            </div>
            <div class="result-item">
              <span class="result-label">最大回撤：</span>
              <span class="result-value">{{ (resultData.max_drawdown * 100).toFixed(2) }}%</span>
            </div>
          </div>

          <!-- 收益相关 -->
          <div class="result-block return-block">
            <h4 class="block-title return-title">收益相关</h4>
            <div class="result-item">
              <span class="result-label">平均每日涨跌幅：</span>
              <span class="result-value">{{ (resultData.average_daily_return * 100).toFixed(2) }}%</span>
            </div>
            <div class="result-item">
              <span class="result-label">总涨跌幅：</span>
              <span class="result-value">{{ (resultData.total_return * 100).toFixed(2) }}%</span>
            </div>
          </div>

          <!-- 成交量相关 -->
          <div class="result-block volume-block">
            <h4 class="block-title volume-title">成交量相关</h4>
            <div class="result-item">
              <span class="result-label">平均成交量：</span>
              <span class="result-value">{{ resultData.average_volume.toLocaleString() }}</span>
            </div>
            <div class="result-item">
              <span class="result-label">最高成交量：</span>
              <span class="result-value">{{ resultData.max_volume.toLocaleString() }}</span>
            </div>
            <div class="result-item">
              <span class="result-label">最低成交量：</span>
              <span class="result-value">{{ resultData.min_volume.toLocaleString() }}</span>
            </div>
          </div>

          <!-- 涨跌天数 -->
          <div class="result-block days-block">
            <h4 class="block-title days-title">涨跌天数</h4>
            <div class="result-item">
              <span class="result-label">上涨天数：</span>
              <span class="result-value">{{ resultData.up_days }}</span>
            </div>
            <div class="result-item">
              <span class="result-label">下跌天数：</span>
              <span class="result-value">{{ resultData.down_days }}</span>
            </div>
          </div>
        </div>
      </el-card>
    </div>

    <div v-if="imageUrl || imageUrl2 || imageUrl3 || imageUrl4" class="grid-container">
      <div v-if="imageUrl" class="grid-item">
        <h3>📈 收盘价趋势图：</h3>
        <img :src="imageUrl" alt="分析图表" />
      </div>

      <div v-if="imageUrl2" class="grid-item">
        <h3>📉 成交量柱状图：</h3>
        <img :src="imageUrl2" alt="第二张图" />
      </div>

      <div v-if="imageUrl3" class="grid-item">
        <h3>📈 日涨跌幅散点图：</h3>
        <img :src="imageUrl3" alt="第三张图" />
      </div>

      <div v-if="imageUrl4" class="grid-item">
        <h3>📉 移动平均线趋势：</h3>
        <img :src="imageUrl4" alt="第四张图" />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { ElMessage } from 'element-plus'
import { useStockStore } from '../stores/useStockStore'
import { fetchAnalysisResults } from '../services/analysis.js'  // 你的接口调用方法

const form = reactive({
  ts_code: '600519.SH',  // 默认示例代码
  start_date: '2024-01-01',
  end_date: '2024-12-31',
})

const stockStore = useStockStore()
const resultData = ref(null)
const imageUrl = ref('')
const imageUrl2 = ref('')
const imageUrl3 = ref('')
const imageUrl4 = ref('')
const isLoading = ref(false)

const onAnalyze = async () => {
  try {
    isLoading.value = true
    const res = await fetchAnalysisResults(form)
    const data = res.data

    resultData.value = data.result
    imageUrl.value = `data:image/png;base64,${data.image_base64_1}`
    imageUrl2.value = `data:image/png;base64,${data.image_base64_2}`
    imageUrl3.value = `data:image/png;base64,${data.image_base64_3}`
    imageUrl4.value = `data:image/png;base64,${data.image_base64_4}`

    // 同步数据到 Pinia
    stockStore.setForm(form)
    stockStore.setRawData(data)

    ElMessage.success('分析完成')
  } catch (error) {
    console.error(error)
    ElMessage.error('分析失败，请检查输入或后端服务')
  } finally {
    isLoading.value = false
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

.header-container {
  margin-bottom: 20px;
  text-align: center;
}

.page-title {
  color: #2c3e50;
  font-weight: 600;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* 表单样式 */
.form-container {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 10px;
  backdrop-filter: blur(8px);
  margin-bottom: 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
    /* 添加以下居中样式 */
  max-width: 500px; /* 可根据需要调整宽度 */
  margin-left: auto;
  margin-right: auto;
}

/* 结果容器 */
.result-container {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 10px;
  backdrop-filter: blur(8px);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  margin-bottom: 20px;
}

.result-card {
  background-color: #f8f9fa;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.section-title {
  font-size: 20px;
  margin-bottom: 18px;
  color: #2c3e50;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

/* 结果网格 */
.result-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: auto auto;
  gap: 24px 30px;
}

/* 结果块样式 */
.result-block {
  background: #ffffff;
  padding: 18px;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
  min-width: 0;
}

/* 各块标题颜色区分 */
.block-title {
  margin-bottom: 12px;
  padding-bottom: 6px;
  font-weight: 700;
  font-size: 1.3em;
  border-bottom: 2px solid;
  text-align: left;
}

.price-title {
  color: #409eff;
  border-color: #409eff;
}

.return-title {
  color: #134f8c;
  border-color: #134f8c;
}

.volume-title {
  color: #2e42c4;
  border-color: #2e42c4;
}

.days-title {
  color: #5c0e5e;
  border-color: #5c0e5e;
}

/* 结果项样式 */
.result-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  padding-bottom: 10px;
  border-bottom: 1px dashed #eee;
}

.result-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.result-label {
  font-weight: 500;
  color: #495057;
}

.result-value {
  font-weight: 600;
  color: #3498db;
}

/* 图表区网格 */
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 20px;
}

.grid-item h3 {
  margin-bottom: 12px;
  font-weight: 700;
  color: #134f8c;
  border-bottom: 2px solid rgba(19, 79, 140, 0.97);
  padding-bottom: 6px;
  text-align: left;
}

.grid-item img {
  max-width: 100%;
  display: block;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgb(0 0 0 / 0.1);
}

/* 表单元素样式 */
.el-form-item > .el-input,
.el-form-item > .el-date-picker {
  width: 100%;
  max-width: 300px;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .page-container {
    padding: 15px;
    margin: 10px;
  }

  .form-container, .result-container {
    padding: 15px;
  }

  .result-card {
    padding: 15px;
  }

  .result-grid {
    grid-template-columns: 1fr;
  }

  .grid-container {
    grid-template-columns: 1fr;
  }

  .el-form-item > .el-input,
  .el-form-item > .el-date-picker {
    max-width: 100%;
  }
}
</style>