import { defineStore } from 'pinia'

export const useStockStore = defineStore('stock', {
  state: () => ({
    form: {
      ts_code: '600519.SH',
      start_date: '2024-01-01',
      end_date: '2024-12-31'
    },
    rawData: null,   // 爬取的数据，分析接口返回的完整数据
    predictionResult: null  // 预测结果
  }),
  actions: {
    setForm(newForm) {
      this.form = { ...newForm }
    },
    setRawData(data) {
      this.rawData = data
    },
    setPredictionResult(result) {
      this.predictionResult = result
    }
  }
})