<template>
    <v-container class="registration">
        <v-text-field v-model="teamname" type="text" placeholder="Enter a name for your team" fluid />
        <button @click="sendData">Register</button>         
</v-container>

</template>
    
    
  
    <script setup>
    import { ref } from 'vue';

    
    const props = defineProps({
      socket: {
        type: Object,
        required: true
      }
    });



    const teamname = ref('');



    async function sendData() {
    console.log(teamname)
    props.socket.emit('register', teamname.value)  
    }


    </script>
    <style scoped>
    .registration{
        display: flex;
        flex-direction: column;
        width: 80%;
    
      }
  
  
  </style>