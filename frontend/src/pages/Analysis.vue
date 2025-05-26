<template>
  <div class="page-container">
    <h2>🏦金融分析页面</h2>

    <el-form :model="form" label-width="100px" class="form-container">
      <el-form-item label="股票代码">
        <el-input v-model="form.stock_code" placeholder="如：600519.SH" style="width: 300px;" />
      </el-form-item>
      <el-form-item label="开始日期">
        <el-date-picker v-model="form.start_date" type="date" placeholder="选择开始日期" format="YYYY-MM-DD" style="width: 300px;" />
      </el-form-item>
      <el-form-item label="结束日期">
        <el-date-picker v-model="form.end_date" type="date" placeholder="选择结束日期" format="YYYY-MM-DD" style="width: 300px;" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onAnalyze">开始分析</el-button>
      </el-form-item>
    </el-form>

    <div v-if="resultData" class="result-container">
      <el-card>
        <h3 class="section-title">📊 分析结果：</h3>
        <div class="result-grid">
          <!-- 价格相关 -->
          <div class="result-block price-block">
            <h4 class="block-title price-title">价格相关</h4>
            <p><strong>平均收盘价：</strong>{{ resultData.average_close.toFixed(2) }}</p>
            <p><strong>最高收盘价：</strong>{{ resultData.max_close.toFixed(2) }}</p>
            <p><strong>最低收盘价：</strong>{{ resultData.min_close.toFixed(2) }}</p>
            <p><strong>波动率（标准差）：</strong>{{ (resultData.volatility * 100).toFixed(2) }}%</p>
            <p><strong>最大回撤：</strong>{{ (resultData.max_drawdown * 100).toFixed(2) }}%</p>
          </div>

          <!-- 收益相关 -->
          <div class="result-block return-block">
            <h4 class="block-title return-title">收益相关</h4>
            <p><strong>平均每日涨跌幅：</strong>{{ (resultData.average_daily_return * 100).toFixed(2) }}%</p>
            <p><strong>总涨跌幅：</strong>{{ (resultData.total_return * 100).toFixed(2) }}%</p>
          </div>

          <!-- 成交量相关 -->
          <div class="result-block volume-block">
            <h4 class="block-title volume-title">成交量相关</h4>
            <p><strong>平均成交量：</strong>{{ resultData.average_volume.toFixed(0) }}</p>
            <p><strong>最高成交量：</strong>{{ resultData.max_volume.toFixed(0) }}</p>
            <p><strong>最低成交量：</strong>{{ resultData.min_volume.toFixed(0) }}</p>
          </div>

          <!-- 涨跌天数 -->
          <div class="result-block days-block">
            <h4 class="block-title days-title">涨跌天数</h4>
            <p><strong>上涨天数：</strong>{{ resultData.up_days }}</p>
            <p><strong>下跌天数：</strong>{{ resultData.down_days }}</p>
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
const imageUrl2 = ref('')
const imageUrl3 = ref('')
const imageUrl4 = ref('')

const onAnalyze = async () => {
  try {
    const res = await fetchAnalysisResults(form.value)
    resultData.value = res.data.result
    imageUrl.value = `data:image/png;base64,${res.data.image_base64_1}`
    imageUrl2.value = `data:image/png;base64,${res.data.image_base64_2}`
    imageUrl3.value = `data:image/png;base64,${res.data.image_base64_3}`
    imageUrl4.value = `data:image/png;base64,${res.data.image_base64_4}`
    ElMessage.success('分析完成')
  } catch (err) {
    console.error(err)
    ElMessage.error('分析失败，请检查输入或后端服务')
  }
}
</script>

<style scoped>
.page-container {
  width: 70vw;       /* 宽度占视口98%，左右留1%空白 */
  max-width: none;   /* 不限制最大宽度 */
  margin: 12px auto;
  padding: 0 4px;
  box-sizing: border-box;
}

h2 {
  font-weight: bold;
  margin-bottom: 20px;
  text-align: center;
}

/* 分析结果外层 */
.result-container el-card {
  padding: 8px;
}

/* 大标题左对齐 */
.section-title {
  margin-bottom: 24px;
  font-weight: 700;
  font-size: 1.8em;
  color: #2c3e50;
  letter-spacing: 1px;
  text-align: left;
}

/* 结果用 grid 两列两行 */
.result-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: auto auto;
  gap: 24px 30px;
}

/* 每个结果块样式 */
.result-block {
  background: #f9f9f9;
  padding: 16px 20px;
  border-radius: 8px;
  box-shadow: 0 0 8px rgb(0 0 0 / 0.1);
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

/* 图表区2列网格 */
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

.el-form-item > .el-input,
.el-form-item > .el-date-picker {
  width: 30%;        /* 输入框和日期选择器都占满父容器宽度 */
}
</style>
