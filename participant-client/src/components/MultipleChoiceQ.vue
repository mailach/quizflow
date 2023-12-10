<script setup lang="ts">
import AnswerBox from './AnswerBox.vue';
import SubmitBtn from './SubmitBtn.vue';
defineProps<{ msg: string, choices: Array<string> }>()
</script>

<template>
  <h1>{{ msg }}</h1>
  <div class="test">
    <AnswerBox v-for="choice in choices" :answer="choice"/>
  </div>
  <SubmitBtn/>
</template>

<style scoped>
h1 {
  color: aqua;
}

div {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>
