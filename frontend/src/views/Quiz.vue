
<template>
  <v-container class="image">
    <MCquestion v-if="status==='mc-question'" :question="question" :options="options" />
    <WaitingScreen v-else gifUrl="https://i.giphy.com/6h5IYmoBn2xYQ.webp" msg="Please wait..."/>


  </v-container>
</template>


<script lang="ts" setup>

import io from 'socket.io-client';
import WaitingScreen from '@/components/WaitingScreen.vue';
import MCquestion from '@/components/MCquestion.vue';

const question = ref([]);
const options = ref([]);
const status = ref([]);

import {ref, onMounted } from 'vue';


const socket = io('http://127.0.0.1:5123/quiz');




onMounted(() => {
  console.log("TEST");
  initializeSocket();
});

// Initialize and manage socket connection
function initializeSocket() {
  console.log("Starting connection to Quiz Server");
  
  socket.on('connect', () => {
    console.log('Connected to quiz server');
  });  


  socket.on('mc-question', (data) => {
    console.log("MC QUESTION FIRED");
    console.log(data)
    question.value = data["text"]
    options.value = data["options"]
    status.value="mc-question"
    console.log(status)
    console.log(status.value==="mc-question")
  });

}
</script>

<style scoped>
</style>


