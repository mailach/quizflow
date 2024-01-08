
<template>
  <v-container class="image">
    <div class="main">
        <transition name="fade">
          <img v-if="showWelcome" class="welcome-message" src="/quizflow.png" />
        </transition>
        <v-btn class="register-btn">Register Team</v-btn>
      </div>
  </v-container>
</template>


<script lang="ts" setup>
import io from 'socket.io-client';
import { ref, onMounted } from 'vue';

const socket = io('http://127.0.0.1:5123/admin');


const showWelcome = ref(true);

onMounted(() => {
  initializeSocket();
});

// Initialize and manage socket connection
function initializeSocket() {
  console.log("Starting connection to WebSocket Server");
  
  socket.on('connect', () => {
    console.log('Connected to webSocket');
  });

  /*
  socket.on('questions', (data) => {
    console.log("Questions received");
    questions.value = data["questions"];
  });

  socket.on('rounds', (data) => {
    console.log("Rounds received");
    console.log("Rounds received");
    rounds.value = data["rounds"];
  });
  */

  
}



</script>

<style scoped>
.welcome-message {
  visibility: visible;
  text-align: center;
  font-size: 2em;
  animation: fadeIn 2s cubic-bezier(0.7, 0, 1, 1); 
}

.register-btn {
  opacity: 0; /* Initially hidden */
  margin-top: 20px;
  animation: fadeInButton 1s cubic-bezier(0.7, 0, 1, 1) 2s forwards; /* Added 'forwards' */
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes fadeInButton {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}


.image{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 100%;
  align-content: center;
}

.main{
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>


