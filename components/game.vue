<template>
  <div class="bg-gray-100 h-full dark:bg-gray-800 p-10">
    <div class="bg-gray-100 dark:bg-gray-800">
      <!-- テキスト選択カード -->
      <div class="h-auto grid place-items-center grid-cols-6 gap-4">
        <div
          v-for="card of txtCards"
          :key="`image-${card.id}`"
          class="w-44 h-44 bg-green-800 border border-green-700 rounded-lg shadow text-white p-4 text-4xl flex items-center justify-center"
          @click="() => !collectIds.includes(card.id) && handleClickText(card)"
          :class="collectIds.includes(card.id) ? '!bg-blue-300 !border-blue-400' : ''"
        >
          {{ card.id }}
        </div>
      </div>
      <!-- 中央ブロック -->
      <div class="my-4 grid place-items-center grid-cols-1 gap-4">
        <div v-if="gaming">
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
      </div>

      <!-- Image選択カード -->
      <div class="h-auto grid place-items-center grid-cols-6 gap-4">
        <div
          v-for="card of imgCards"
          :key="`text-${card.id}`"
          class="w-44 h-44 border rounded-lg shadow bg-pink-800 border-pink-700 text-white p-4 text-4xl flex items-center justify-center"
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
import { CARDS_MASTER, baseUrl } from '../master'
import { sampleSize, shuffle } from 'lodash'
export type Game = { seconds: number; cardNumber: number; name: string }

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
const cards = ref(
  sampleSize(
    CARDS_MASTER.map((card: any, index: number) => {
      return { ...card, url: baseUrl + card.url, id: index + 1 } as Card
    }) as Card[],
    game.value.cardNumber
  )
)
const txtCards = ref<Card[]>([])
const imgCards = ref<Card[]>([])

const collectIds = ref<number[]>([])

const timerId = ref<NodeJS.Timer>()
const gaming = ref(false)
const gameStart = () => {
  gaming.value = true
  txtCards.value = shuffle(cards.value)
  imgCards.value = shuffle(cards.value)
  timer(true)
}
const gameOver = () => {
  timer(false)
  gaming.value = false
}
const timer = (start: boolean) => {
  if (start) {
    timerId.value = setInterval(() => {
      game.value.seconds++
    }, 1000)
  } else {
    clearInterval(timerId.value!)
  }
}
const collect = () => {
  if (!selectImgId.value || !selectTxtId.value) {
    return
  }
  if (selectImgId.value === selectTxtId.value) {
    collectIds.value.push(selectImgId.value)
  }
  selectImgId.value = selectTxtId.value = undefined
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
  cards.value = sampleSize(
    CARDS_MASTER.map((card: any, index: number) => {
      return { ...card, url: baseUrl + card.url, id: index + 1 } as Card
    }) as Card[],
    game.value.cardNumber
  )
  txtCards.value = shuffle(cards.value)
  imgCards.value = shuffle(cards.value)
  gameStart()
}

gameStart()
</script>
