Copy code
<template>
  <div id="app">
    <h1>Welcome Admin!</h1>
    <button @click="showNewQuestionForm = !showNewQuestionForm">
      New Question
    </button>
    <NewQuestion 
      v-if="showNewQuestionForm" 
      :socket="this.socket" 
      @question-added="handleQuestionAdded" />
    <QuestionList :questions="questions" />
  </div>
</template>
<script>
import io from 'socket.io-client';
import axios from 'axios'; // Import Axios

import NewQuestion from './components/NewQuestion.vue';
import QuestionList from './components/QuestionList.vue';

export default {
  name: 'App',
  components: {
    NewQuestion,
    QuestionList
  },
  data() {
    return {
      socket: null,
      showNewQuestionForm: false,
      questions: [] // Initialize the questions array
    };
  },
  created: function() {
    this.initializeSocket();
    this.fetchQuestions();
  },
  methods: {
    initializeSocket() {
      console.log("Starting connection to WebSocket Server");
      this.socket = io.connect('http://127.0.0.1:5123/admin');
    
      this.socket.on('connect', function () {
        console.log('Connected to webSocket');
        this.socket.emit('test', {});
      }.bind(this));

      this.socket.on('status', function(data) {
        console.log("STATUS RECEIVED")
        console.log(data)
      }.bind(this));
    },
    async fetchQuestions() {
      try {
        const response = await axios.get('http://backend:5123/questions');
        this.questions = response.data;
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    },
    handleQuestionAdded() {
      this.fetchQuestions(); // Fetch updated questions
      this.showNewQuestionForm = false; // Hide the form
    }
  } // Added missing closing bracket for methods
}
</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>