<template>
  <div class="page-container">
    <div class="header-container">
      <h2 class="page-title">🔮机器学习预测</h2>
    </div>

    <el-form label-width="100px" class="form-container">
      <el-form-item label="股票代码">
        <el-input :model-value="form.ts_code" disabled style="width: 300px;" />
      </el-form-item>
      <el-form-item label="开始日期">
        <el-date-picker :model-value="form.start_date" type="date" disabled style="width: 300px;" />
      </el-form-item>
      <el-form-item label="结束日期">
        <el-date-picker :model-value="form.end_date" type="date" disabled style="width: 300px;" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onPredict" :disabled="!form.ts_code">开始预测</el-button>
      </el-form-item>
    </el-form>

    <div v-if="predictionResult" class="result-container">
      <el-card shadow="hover" class="result-card">
        <h3 class="section-title">🔍 预测结果</h3>

        <el-card shadow="never" class="sub-card main-card">
          <h4>📊 最新预测</h4>
          <div class="prediction-item">
            <span class="prediction-label">下一日收盘价预测（线性回归）：</span>
            <span class="prediction-value">{{ predictionResult['最新预测']['下一日收盘价预测（线性回归）'].toFixed(2) }}</span>
          </div>
          <div class="prediction-item">
            <span class="prediction-label">下一日收盘价预测（随机森林）：</span>
            <span class="prediction-value">{{ predictionResult['最新预测']['下一日收盘价预测（随机森林）'].toFixed(2) }}</span>
          </div>
          <div class="prediction-item">
            <span class="prediction-label">下一日是否上涨预测（逻辑回归）：</span>
            <span class="prediction-value">{{ predictionResult['最新预测']['下一日是否上涨预测（逻辑回归）'] }}</span>
          </div>
          <div class="prediction-item">
            <span class="prediction-label">下一日是否上涨预测（SVM）：</span>
            <span class="prediction-value">{{ predictionResult['最新预测']['下一日是否上涨预测（SVM）'] }}</span>
          </div>
        </el-card>

        <el-card shadow="never" class="sub-card main-card">
          <h4>📉 回归模型评估</h4>
          <div class="evaluation-item">
            <span class="evaluation-label">线性回归 MSE：</span>
            <span class="evaluation-value">{{ predictionResult['回归模型评估']['线性回归'].MSE.toFixed(2) }}</span>
          </div>
          <div class="evaluation-item">
            <span class="evaluation-label">线性回归 R2：</span>
            <span class="evaluation-value">{{ predictionResult['回归模型评估']['线性回归'].R2.toFixed(3) }}</span>
          </div>
          <div class="evaluation-item">
            <span class="evaluation-label">随机森林回归 MSE：</span>
            <span class="evaluation-value">{{ predictionResult['回归模型评估']['随机森林回归'].MSE.toFixed(2) }}</span>
          </div>
          <div class="evaluation-item">
            <span class="evaluation-label">随机森林回归 R2：</span>
            <span class="evaluation-value">{{ predictionResult['回归模型评估']['随机森林回归'].R2.toFixed(3) }}</span>
          </div>
        </el-card>

        <el-card shadow="never" class="sub-card main-card">
          <h4>📈 分类模型评估</h4>
          <div class="evaluation-item">
            <span class="evaluation-label">逻辑回归 准确率：</span>
            <span class="evaluation-value">{{ (predictionResult['分类模型评估']['逻辑回归'].准确率 * 100).toFixed(2) }}%</span>
          </div>
          <div class="evaluation-item">
            <span class="evaluation-label">支持向量机 准确率：</span>
            <span class="evaluation-value">{{ (predictionResult['分类模型评估']['支持向量机'].准确率 * 100).toFixed(2) }}%</span>
          </div>
        </el-card>
      </el-card>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useStockStore } from '../stores/useStockStore'
import { fetchPredictionResults } from '../services/prediction'
import { ElMessage } from 'element-plus'

const stockStore = useStockStore()
const form = ref({
  ts_code: '',
  start_date: '',
  end_date: ''
})
const predictionResult = ref(null)

onMounted(() => {
  if (stockStore.form.ts_code) {
    form.value = { ...stockStore.form }
  } else {
    ElMessage.warning('请先在分析页面输入参数并完成分析')
  }
})

const onPredict = async () => {
  try {
    const res = await fetchPredictionResults(form.value)
    predictionResult.value = res
    stockStore.setPredictionResult(res.data)
    ElMessage.success('预测完成')
  } catch (error) {
    console.error(error)
    ElMessage.error('预测失败，请稍后重试')
  }
}
</script>

<style scoped>
/* 毛玻璃效果 */
.page-container {
  max-width: 900px;
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

.result-container {
  background-color: rgba(255, 255, 255, 0.7);
  padding: 20px;
  border-radius: 10px;
  backdrop-filter: blur(8px);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
}

.result-card {
  background-color: #f8f9fa;
  border-radius: 12px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.sub-card {
  margin-bottom: 20px;
  padding: 18px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.main-card {
  background-color: #e6f2ff;
  border: 1px solid #91caff;
  box-shadow: 0 4px 12px rgba(145, 204, 255, 0.3);
}

.section-title {
  font-size: 20px;
  margin-bottom: 18px;
  color: #2c3e50;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.05);
}

.prediction-item, .evaluation-item {
  display: flex;
  justify-content: space-between;
  margin-bottom: 12px;
  padding-bottom: 12px;
  border-bottom: 1px dashed #eee;
}

.prediction-item:last-child, .evaluation-item:last-child {
  border-bottom: none;
  margin-bottom: 0;
  padding-bottom: 0;
}

.prediction-label, .evaluation-label {
  font-weight: 500;
  color: #495057;
}

.prediction-value, .evaluation-value {
  font-weight: 600;
  color: #3498db;
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
}
</style>