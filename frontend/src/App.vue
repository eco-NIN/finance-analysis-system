<!-- frontend/src/App.vue -->
<!--统一布局（App.vue）-->
<template>
  <el-container>
    <el-header>
      <el-menu mode="horizontal" router>
        <el-menu-item index="/">首页</el-menu-item>
        <el-menu-item index="/crawler">获取股票基础信息</el-menu-item>
        <el-menu-item index="/analysis">金融数据图像分析</el-menu-item>
        <el-menu-item index="/prediction">金融数据预测</el-menu-item>
        <el-menu-item index="/dongfang">东方财富金融数据爬取与预测</el-menu-item>
      </el-menu>
    </el-header>
    <el-main>
      <router-view />
    </el-main>
  </el-container>
</template>

<script setup>
</script>

<style>
body {
  margin: 0;
  font-family: 'Helvetica Neue', Arial, sans-serif;
}
</style>