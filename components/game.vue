<template>
  <div class="bg-gray-100 h-full dark:bg-gray-200 p-10">
    <div class="bg-gray-100 dark:bg-gray-200">
      <!-- テキスト選択カード -->
      <div class="h-auto grid place-items-center grid-cols-6 gap-4">
        <div
          v-for="card of txtCards"
          :key="`image-${card.id}`"
          class="w-44 h-44 bg-green-800 border border-green-700 rounded-lg shadow text-green-800 p-4 text-4xl flex items-center justify-center"
          @click="() => !collectIds.includes(card.id) && handleClickText(card)"
          :class="collectIds.includes(card.id) ? '!bg-blue-300 !border-blue-400' : ''"
        >
          {{ card.id }}
        </div>
      </div>
      <!-- 中央ブロック -->
      <div v-if="gaming" class="my-4 grid place-items-center grid-cols-1 gap-4">
        <div class="relative">
          <div class="absolute top-[30%] left-[105%] w-80 h-80">
            <div v-if="collected">
              <div class="text-7xl">🙆🏻 正解！</div>
            </div>
            <div v-if="collected === false">
              <div class="text-7xl">🙅🏻 残念〜</div>
            </div>
          </div>
          <div class="max-w-sm border rounded-lg shadow bg-green-800 border-green-700">
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

              <nuxt-img v-else src="./sample.png" sizes="sm:100vw md:20vw lg:300px" />
            </div>
            <div class="bg-pink-800 p-5">
              <div>
                <nuxt-img v-if="selectImg" :src="selectImg" sizes="sm:100vw md:20vw lg:300px" />
                <nuxt-img v-else src="./sample.png" sizes="sm:100vw md:20vw lg:300px" />
              </div>
            </div>
          </div>
          <div>{{ game.seconds }}</div>
        </div>
      </div>
      <div v-else class="h-80 p-4 text-4xl">
        🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉<br />
        {{ game.name }}さんのスコア<br />
        <div>
          <span class="text-5xl">
            {{ game.cardNumber }}
          </span>
          <span class="text-3xl text-gray-600"> 名水</span>：<span class="text-5xl">{{ game.seconds }}</span>
          <span class="text-3xl text-gray-600"> 秒 </span>
        </div>
        🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
        <div>
          <button
            @click="() => replay()"
            type="button"
            class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-full text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700"
          >
            再JACKする
          </button>
        </div>
      </div>

      <!-- Image選択カード -->
      <div class="h-auto grid place-items-center grid-cols-6 gap-4">
        <div
          v-for="card of imgCards"
          :key="`text-${card.id}`"
          class="w-44 h-44 border rounded-lg shadow bg-pink-800 border-pink-700 text-pink-800 p-4 text-4xl flex items-center justify-center"
          @click="() => !collectIds.includes(card.id) && handleClickImage(card)"
          :class="collectIds.includes(card.id) ? '!bg-blue-300 !border-blue-400' : ''"
        >
          {{ card.id }}
        </div>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
console.log('start 0')

const baseUrl = 'https://water-pub.env.go.jp/water-pub/contents/meisui/image'
const CARDS_MASTER = [
  {
    url: '/8020071217103528/w080m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '四万十川（しまんとがわ）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/220071204093601/w002m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '甘露泉水（かんろせんすい）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/320071203095601/w003m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: 'ナイベツ川湧水（ないべつがわゆうすい）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/420100202110558/w004m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '富田の清（とみたのしつこ）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/520071203100447/w005m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '渾神の清（いがみのしつこ）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/620131105105731/w006m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '龍泉洞地底湖の水（りゅうせんどうちていこのみず）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/720100128141545/w007m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '金沢清水（かなざわしみず）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/1620100212160945/w016m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '八溝川湧水群（やみぞがわゆうすいぐん）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/1720071203105911/w017m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '出流原弁天池湧水（いずるはらべんてんいけゆうすい）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/1820071203110314/w018m.JPG',
    category: '河川',
    place: '高知県県西部',
    name: '尚仁沢湧水（しょうじんざわゆうすい）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/1920071203111121/w019m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '雄川堰（おがわぜき）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
  {
    url: '/2020071203111516/w020m.jpg',
    category: '河川',
    place: '高知県県西部',
    name: '水島湧水（はこしまゆうすい）',
    description:
      '流域面積の85％が森林で、人工改変度が小さい。中流域は流れが激しい蛇行を繰り返し、それは多くの瀬や淵を作り、豊かな自然景観が残る。天然アユの漁場としても名高く、火を振りながら追い込む火振り漁は独特のものである。',
  },
]

type Game = { seconds: number; cardNumber: number; name: string }

const props = defineProps({
  name: String,
  cardNumber: Number,
})
const game = ref<Game>({ seconds: 0, cardNumber: props.cardNumber!, name: props.name! })

type Card = { id: number; url: string; category: string; place: string; name: string; description: string }
const selectImgId = ref<number>()
const selectTxtId = ref<number>()
const selectImg = computed(() => imgCards.value.find(({ id }) => id === selectImgId.value)?.url)
const selectTxt = computed(() => txtCards.value.find(({ id }) => id === selectTxtId.value))

const shuffle = (array: Card[]) => {
  for (let i = array.length - 1; i >= 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[array[i], array[j]] = [array[j], array[i]]
  }
  return array
}

const cards = ref(
  CARDS_MASTER.map((card: any, index: number) => {
    return { ...card, url: baseUrl + card.url, id: index + 1 } as Card
  }) as Card[]
)
const txtCards = ref<Card[]>([])
const imgCards = ref<Card[]>([])

const collectIds = ref<number[]>([])

const timerId = ref<number>()
const gaming = ref(false)
const collected = ref<boolean>()
const gameStart = () => {
  console.log('start 2')

  gaming.value = true
  txtCards.value = shuffle(cards.value)
  imgCards.value = shuffle(cards.value)
  timer(true)
  console.log('start 3')
}
const gameOver = () => {
  timer(false)
  gaming.value = false
}
const timer = (start: boolean) => {
  if (start) {
    timerId.value = window.setInterval(() => {
      game.value.seconds++
    }, 1000)
  } else {
    window.clearInterval(timerId.value!)
  }
}
const collect = () => {
  if (!selectImgId.value || !selectTxtId.value) {
    return
  }
  collected.value = selectImgId.value === selectTxtId.value
  if (selectImgId.value === selectTxtId.value) {
    collectIds.value.push(selectImgId.value)
  }

  window.setTimeout(() => {
    collected.value = undefined
    selectImgId.value = selectTxtId.value = undefined
  }, 2000)
}
const result = () => {
  if (collectIds.value.length < game.value.cardNumber) {
    return
  }
  gameOver()
}
const handleClickText = (card: Card) => {
  selectTxtId.value = card.id
  collect()
  result()
}
const handleClickImage = (card: Card) => {
  selectImgId.value = card.id
  collect()
  result()
}
const replay = () => {
  collectIds.value = []
  game.value = { name: props.name!, cardNumber: props.cardNumber!, seconds: 0 }
  cards.value = CARDS_MASTER.map((card: any, index: number) => {
    return { ...card, url: baseUrl + card.url, id: index + 1 } as Card
  }) as Card[]
  txtCards.value = shuffle(cards.value)
  imgCards.value = shuffle(cards.value)
  gameStart()
}

gameStart()
</script>
