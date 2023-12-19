
<template>
      <h1>Welcome Admin!</h1>
        <v-btn @click="showNewQuestionForm = !showNewQuestionForm">
          New Question
        </v-btn>
        <NewQuestion 
          v-if="showNewQuestionForm" 
          :socket="socket" 
          @question-added="handleQuestionAdded" />
      <QuestionList :questions="questions" />
</template>

<script lang="ts" setup>
console.log("TEST")
import io from 'socket.io-client';
import QuestionList from '@/components/QuestionList.vue';
import NewQuestion from '@/components/NewQuestion.vue';
import { ref, onMounted } from 'vue';

// Define reactive variables
const questions = ref([]);
let showNewQuestionForm = ref(false);
const socket = io('http://127.0.0.1:5123/admin');

onMounted(() => {
  initializeSocket();
});

// Initialize and manage socket connection
function initializeSocket() {
  console.log("Starting connection to WebSocket Server");
  
  socket.on('connect', () => {
    console.log('Connected to webSocket');
    socket.emit('get-questions');
    console.log("Questions requested...");
  });

  socket.on('questions', (data) => {
    console.log("Questions received");
    questions.value = data["questions"];
  });

  
}
function handleQuestionAdded() {
      this.showNewQuestionForm = false; 
    }



</script>
