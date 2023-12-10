<script setup lang="ts">
import SubmitBtn from './SubmitBtn.vue';
</script>

<template>
  <h1>Team registration</h1>
  <input type="text" placeholder="Enter your name" />
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
