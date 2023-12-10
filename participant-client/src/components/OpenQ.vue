<script setup lang="ts">
import SubmitBtn from './SubmitBtn.vue';
defineProps<{ msg: string}>()
</script>

<template>
  <h1>{{ msg }}</h1>
  <input type="text" placeholder="Enter your response" />
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
