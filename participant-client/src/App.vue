<template>
  <div id="app">
    <button @click="toggleDisplay">Toggle Display</button>
    <GIFDisplay v-if="showGIF" :gifUrl="gifUrl" />
    <Question v-else :questionData="questionData"/>
    <TeamRegistration />
  </div>
</template>

<script>
import GIFDisplay from './components/GIFDisplay.vue';
import Question from './components/Question.vue'
import TeamRegistration from './components/TeamRegistration.vue';
import io from 'socket.io-client';

sessionStorage.setItem('testkey', 'testvalue');
console.log(sessionStorage.getItem("testkey"));

export default {
  name: 'App',
  components: {
    GIFDisplay,
    Question, 
    TeamRegistration 
  },
  data: function() {
    return {
      showGIF: true, // Controls which component is displayed
      gifUrl: "https://media0.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif?cid=ecf05e47za6fq6olphuwm5sk5mr5ootfaaku6i51o3ft4kap&ep=v1_gifs_search&rid=giphy.gif&ct=g",
      connection: null,
      questionData: {"type": "multiple-choice", "msg": "Example open message?", "choices": ['Testanswer 1', 'Testanswer 2', 'Testanswer 3', 'Testanswer 4']}
    }
  },
  methods: {
    toggleDisplay() {
      this.showGIF = !this.showGIF;
    },
    sendMessage: function(message) {
      console.log(message);
      console.log(this.connection);
      this.connection.send(message);
    }
  },
  created: function() {
    console.log("Starting connection to WebSocket Server");
    const socket = io.connect('http://127.0.0.1:5123/');
    
    socket.on('connect', function () {
      console.log('Connected to webSocket');
      //sending to server
      socket.emit('test', {});
    });

    socket.on('status', function(data) {
                console.log("STATUS RECEIVED")
                console.log(data)
                });
  }  
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