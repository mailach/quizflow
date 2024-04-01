<template>
    <v-container class="waiting">
        <!-- Bind the src attribute to the gifUrl prop -->
        <div class="gif-div">
        <h1>{{msg}}</h1>
        <img :src="gifUrl" alt="Loading GIF" class="gif" />
      </div>
    </v-container>

</template>
    
    

<script setup>
import { defineProps } from 'vue';

// Define the props this component expects
const props = defineProps({
  gifUrl: String,
  msg: String

});


</script>
<style scoped>
.gif-div{
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
}

.gif{
  max-width: 70%;
}

</style>