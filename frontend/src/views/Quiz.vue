
<template>
  <v-container class="image">
    <WaitingScreen gifUrl="https://i.giphy.com/6h5IYmoBn2xYQ.webp" msg="Please wait..."/>
  </v-container>
</template>


<script lang="ts" setup>
import WaitingScreen from '@/components/WaitingScreen.vue';

console.log(localStorage.team)
</script>

<style scoped>
</style>


