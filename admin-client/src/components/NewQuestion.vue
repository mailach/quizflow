<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12" md="8">
          <h2>Create New Question</h2>
          <v-form @submit.prevent="submitQuestion">
            <v-text-field
              label="Quiz Round"
              v-model.number="question.round"
              type="number"
              required
            ></v-text-field>
  
            <v-text-field
              label="Question ID"
              v-model="question.id"
              required
            ></v-text-field>
  
            <v-text-field
              label="Question Text"
              v-model="question.text"
              required
            ></v-text-field>
  
            <v-text-field
              v-for="(option, index) in options"
              :key="index"
              :label="'Answer ' + (index + 1)"
              v-model="question.options[index]"
              required
            ></v-text-field>
  
            <v-select
              label="Correct Answer"
              :items="options"
              item-text="option"
              item-value="index"
              v-model="question.correctAnswer"
            ></v-select>
  
            <v-text-field
              label="Points"
              v-model.number="question.points"
              type="number"
              required
            ></v-text-field>
  
            <v-btn type="submit" color="primary">Submit Question</v-btn>
          </v-form>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import { defineProps } from 'vue';
  
  // Define props
  const props = defineProps({
    socket: {
      type: Object,
      required: true
    }
  });
  
  // Reactive state
  const question = ref({
    id: '',
    text: '',
    options: Array(4).fill(''),
    correctAnswer: 0,
    points: 0,
    round: 0,
  });
  const options = ref([1, 2, 3, 4]);
  
  // Methods
  const submitQuestion = () => {
    props.socket.emit('create-question', question.value);
    console.log('Question submitted:', question.value);
    resetForm();
    // Emit event
  };
  
  const resetForm = () => {
    question.value = {
      id: '',
      text: '',
      options: Array(4).fill(''),
      correctAnswer: 0,
      points: 0,
      round: 0,
    };
  };
  </script>
  
  <style scoped>
    /* Vuetify styles and any custom styles */
  </style>
  