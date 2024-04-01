<template>
    <v-container class="waiting">
        <!-- Bind the src attribute to the gifUrl prop -->
        <h1>{{question}}</h1>
        <div> {{options}}</div>
    </v-container>

</template>
    
    

<script setup>
import { defineProps } from 'vue';

// Define the props this component expects
const props = defineProps({
  question: String,
  options: Array

});


</script>
<style scoped>

</style>