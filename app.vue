<template>
  <div class="bg-gray-100 h-full dark:bg-gray-800 p-10">
    <div class="bg-gray-100 dark:bg-gray-800">
      <h1
        class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"
      >
        神経<span class="text-blue-400 text-7xl">水</span>JACK<span class="text-blue-400">！！</span>
      </h1>
      <div v-if="!start">
        <div class="text-7xl text-center my-5 text-gray-600">名水探しに行きませんか？</div>
        お名前
        <input type="text" class="mr-2" v-model="userName" />
        <button
          type="button"
          class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-full text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700"
          @click="() => (start = true)"
        >
          JACK開始！
        </button>
      </div>
      <game v-if="start" :name="userName" :card-number="12" />
    </div>
  </div>
</template>
<script setup lang="ts">
const start = ref(false)
const userName = ref('ななしの名水')
</script>
