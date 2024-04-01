
<template>
    <TeamRegistration v-if="!isRegistered" :socket="socket"/>
    <WaitingScreen v-else gifUrl="https://i.giphy.com/6h5IYmoBn2xYQ.webp" msg="Please wait..."/>
  </template>
  
  <script lang="ts" setup>
import io from 'socket.io-client';
import TeamRegistration from '@/components/TeamRegistration.vue';
import WaitingScreen from '@/components/WaitingScreen.vue';


import {ref, onMounted } from 'vue';


const socket = io('http://127.0.0.1:5123/register');
const isRegistered = ref(false);




onMounted(() => {
  console.log("TEST");
  initializeSocket();
});

// Initialize and manage socket connection
function initializeSocket() {
  console.log("Starting connection to Registration Server");
  
  socket.on('connect', () => {
    console.log('Connected to registration server');
  });  


  socket.on('registration', (data) => {
    console.log("Questions received");
    console.log(data)
  });

  socket.on('waiting', (data) => {
    console.log("Waiting received");
    console.log(data)
    isRegistered.value=true;

  })

  socket.on('activation', (data) => {
    console.log("Activation received");
    localStorage.team = "testestest";
    location.href="quiz"

  })
}

  </script>
  
  <style scoped>
  </style>
  
  
  