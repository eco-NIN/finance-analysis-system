<!--
@Author  : eco
@Date    :2025/5/22 11:01
@Function:搭建一个简单的首页 Home.vue
-->

<template>
  <div class="home">
    <el-container>
      <el-header>
        <h2>金融数据分析系统</h2>
      </el-header>
      <el-main>
        <el-row :gutter="20">
          <el-col :span="8">
            <el-card shadow="hover">
              <h3>数据爬虫</h3>
              <p>获取最新的金融数据。</p>
              <el-button type="primary" @click="goTo('crawler')">进入</el-button>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover">
              <h3>金融分析</h3>
              <p>数据清洗、统计、可视化分析。</p>
              <el-button type="success" @click="goTo('analysis')">进入</el-button>
            </el-card>
          </el-col>
          <el-col :span="8">
            <el-card shadow="hover">
              <h3>机器学习预测</h3>
              <p>构建模型，预测市场趋势。</p>
              <el-button type="warning" @click="goTo('prediction')">进入</el-button>
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