
<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12">
      <QuestionList :rounds="rounds" :questions="questions" :socket="socket" />
      <TeamList :teams="teams" :socket="socket" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang="ts" setup>
import io from 'socket.io-client';
import QuestionList from '@/components/QuestionList.vue';
import TeamList from '@/components/TeamList.vue';

import { ref, onMounted } from 'vue';

// Define reactive variables
const questions = ref([]);
const rounds = ref([]);
const teams = ref([]);

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
    socket.emit('get-rounds');
    socket.emit('get-teams')
    console.log("Questions, rounds, teams requested...");
  });

  socket.on('questions', (data) => {
    console.log("Questions received");
    questions.value = data["questions"];
  });

  socket.on('rounds', (data) => {
    console.log("Rounds received");
    console.log("Rounds received");
    rounds.value = data["rounds"];
  });

  socket.on('teams', (data) => {
    console.log("Teams received");
    console.log(data)
    teams.value=data["teams"]
    //rounds.value = data["rounds"];
  });

  
}



</script>
