<script setup lang="ts">
defineProps<{ answer: string }>()
</script>

<template>
  <button>{{ answer }}</button>
</template>

<style scoped>
button {
  width: 100%;
  height: 50px;
  margin: 5px;
}
</style>
