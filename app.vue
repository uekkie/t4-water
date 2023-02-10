<template>
  <div class="bg-gray-100 h-full dark:bg-gray-800 p-10">
    <div class="bg-gray-100 dark:bg-gray-800">
      <h1
        class="mb-4 text-4xl font-extrabold leading-none tracking-tight text-gray-900 md:text-5xl lg:text-6xl dark:text-white"
      >
        神経水JACK！！
      </h1>

      <div class="h-56 grid place-items-center grid-cols-3 gap-4">
        <div
          v-for="card of cards"
          class="w-44 h-44 bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700 text-white p-4 text-4xl flex items-center justify-center"
          @click="() => (selectTxtId = card.id)"
        >
          {{ card.id }}
        </div>
      </div>
      <div class="flex justify-center">
        <div class="max-w-sm bg-white border border-gray-200 rounded-lg shadow dark:bg-gray-800 dark:border-gray-700">
          <a href="#">
            <img class="rounded-t-lg" src="/docs/images/blog/image-1.jpg" alt="" />
          </a>
          <div class="p-5">
            <div v-if="selectTxt">
              <a href="#">
                <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">
                  {{ selectTxt.name }}
                </h5>
              </a>

              <p class="mb-3 font-normal text-gray-700 dark:text-gray-400">
                {{ selectTxt.description }}
              </p>
            </div>
          </div>
          <div class="dark:bg-pink-800 p-5">
            <div>
              <nuxt-img v-if="selectImg" :src="selectImg" sizes="sm:100vw md:20vw lg:300px" />
              <span v-else class="text-white">カードを選んでね</span>
            </div>
          </div>
        </div>
      </div>

      <div class="h-56 grid place-items-center grid-cols-3 gap-4">
        <div
          v-for="card of cards"
          class="w-44 h-44 bg-white border border-gray-200 rounded-lg shadow dark:bg-pink-800 dark:border-pink-700 text-white p-4 text-4xl flex items-center justify-center"
          @click="() => (selectImgId = card.id)"
        >
          {{ card.id }}
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
const selectImgId = ref<string>()
const selectTxtId = ref<string>()
const selectImg = computed(() => cards.find(({ id }) => id === selectImgId.value)?.url)
const selectTxt = computed(() => cards.find(({ id }) => id === selectTxtId.value))
const cards = [
  {
    id: '1',
    url: 'https://water-pub.env.go.jp/water-pub/contents/meisui/image/8020071217103528/w080m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '四万十川（しまんとがわ）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    id: '2',
    url: 'https://water-pub.env.go.jp/water-pub/contents/meisui/image/8020071217103528/w080m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '四万十川（しまんとがわ）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    id: '3',
    url: 'https://water-pub.env.go.jp/water-pub/contents/meisui/image/8020071217103528/w080m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '四万十川（しまんとがわ）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
]
</script>
