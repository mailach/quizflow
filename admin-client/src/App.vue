<template>
  <div id="app">
    <h1>Welcome Admin!</h1>    
    <NewQuestion :socket="this.socket" />
  </div>
</template>
<script>
import io from 'socket.io-client';

import NewQuestion from './components/NewQuestion.vue';


export default {
  name: 'App',
  components: {
    NewQuestion
  },
  data() {
    return {
      socket: null, // Initialize socket as null
    };
  },
  created: function() {
    console.log("Starting connection to WebSocket Server");
    this.socket = io.connect('http://127.0.0.1:5123/');
    
    this.socket.on('connect', function () {
      console.log('Connected to webSocket');
      //sending to server
      this.socket.emit('test', {});
    }.bind(this));

    this.socket.on('status', function(data) {
                console.log("STATUS RECEIVED")
                console.log(data)
                }.bind(this));
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