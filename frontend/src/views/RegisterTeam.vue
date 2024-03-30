
<template>
    <v-container class="registration">
            <v-text-field v-model="teamname" type="text" placeholder="Enter a name for your team" fluid />
            <button @click="sendData">Register</button>         
    </v-container>
  </template>
  
  
  <script lang="ts" setup>
import io from 'socket.io-client';
import { ref, onMounted } from 'vue';
import axios from 'axios';


const socket = io('http://127.0.0.1:5123/register');



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
}


const teamname = ref('');



async function sendData() {
  console.log(teamname)
  socket.emit('register', teamname.value)  
}


  </script>
  
  <style scoped>


  .registration{
    display: flex;
    flex-direction: column;
    width: 80%;

  }
  </style>
  
  
  