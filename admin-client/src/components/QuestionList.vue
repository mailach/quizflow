<template>
    <div>
      <h2>Existing Questions</h2>
      <ul>
        <li v-for="question in questions" :key="question.id">
          {{ question.text }} - Points: {{ question.points }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'QuestionList',
    data() {
      return {
        questions: []
      };
    },
    created() {
      this.fetchQuestions();
    },
    methods: {
      async fetchQuestions() {
        try {
          const response = await axios.get('http://127.0.0.1:5123/admin/questions');
          this.questions = response.data;
        } catch (error) {
          console.error('Error fetching questions:', error);
        }
      }
    }
  }
  </script>
  