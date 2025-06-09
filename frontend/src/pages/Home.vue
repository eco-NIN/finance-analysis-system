<!--
@Author  :郭宇哲
@Date    :2025/5/22 11:01
@Function:首页Home.vue
-->

<template>
  <div class="home">
    <el-container>
      <el-header>
        <h2>金融数据分析系统</h2>
      </el-header>
      <el-main>
        <el-row :gutter="20">
          <el-col :span="6">
            <el-card shadow="hover">
              <h3>股票数据信息</h3>
              <p>爬取最新的股票数据信息</p>
              <el-button type="primary" @click="goTo('crawler')">进入</el-button>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              <h3>金融数据分析</h3>
              <p>数据清洗、统计、可视化分析</p>
              <el-button type="success" @click="goTo('analysis')">进入</el-button>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              <h3>金融数据预测</h3>
              <p>构建模型，预测市场趋势</p>
              <el-button type="warning" @click="goTo('prediction')">进入</el-button>
            </el-card>
          </el-col>
          <el-col :span="6">
            <el-card shadow="hover">
              <h3>东方财富数据预测</h3>
              <p>爬取 + 清洗 + 预测一体化</p>
              <el-button type="danger" @click="goTo('dongfang')">进入</el-button>
            </el-card>
          </el-col>
        </el-row>
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'
const router = useRouter()
const goTo = (page) => {
  router.push(`/${page}`)
}
</script>

<style scoped>
.home {
  padding: 40px;
}
</style>