<template>
    <div>
      <h2>Create New Question</h2>
      <form @submit.prevent="submitQuestion">
        <div>
          <label>Question ID:</label>
          <input v-model="question.id" type="text" required>
        </div>
        <div>
          <label>Question Text:</label>
          <input v-model="question.text" type="text" required>
        </div>
        <div v-for="(option, index) in options" :key="index">
          <label>Answer {{ index + 1 }}:</label>
          <input v-model="question.options[index]" type="text" required>
        </div>
        <div>
          <label>Correct Answer:</label>
          <select v-model="question.correctAnswer">
            <option v-for="(option, index) in options" :key="index" :value="index">
              {{ option }}
            </option>
          </select>
        </div>
        <div>
          <label>Points:</label>
          <input v-model.number="question.points" type="number" required>
        </div>
        <button type="submit">Submit Question</button>
      </form>
    </div>
  </template>
  <script>
  export default {
    name: 'NewQuestion',
    props: {
      socket: {
        type: Object,
        required: true
      }
    },
    data() {
      return {
        question: {
          id: '',
          text: '',
          options: Array(4).fill(''),
          correctAnswer: 0,
          points: 0
        },
        options: [1, 2, 3, 4]
      };
    },
    methods: {
      submitQuestion() {
        this.socket.emit('newQuestion', this.question);
        console.log('Question submitted:', this.question);
        this.resetForm();
      },
      resetForm() {
        this.question = {
          id: '',
          text: '',
          options: Array(4).fill(''),
          correctAnswer: 0,
          points: 0
        };
      }
    }
  }
  </script>
  <style>
  /* General Styles */
  div {
    font-family: 'Arial', sans-serif;
    max-width: 600px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  h2 {
    color: #333;
    text-align: center;
    margin-bottom: 20px;
  }
  
  /* Form Elements */
  form {
    display: grid;
    grid-gap: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    color: #555;
  }
  
  input[type="text"], input[type="number"], select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
  }
  
  input[type="text"]:focus, input[type="number"]:focus, select:focus {
    border-color: #007bff;
    outline: none;
  }
  
  /* Button Styles */
  button {
    background-color: #007bff;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  /* Responsive Design */
  @media (max-width: 600px) {
    div {
      width: 90%;
      margin: 10px;
      padding: 10px;
    }
  }
  </style>
  
  