<template>
  <div id="app">
    <h1>Welcome Admin!</h1>    
  </div>
</template>
<script>
import io from 'socket.io-client';

export default {
  name: 'App',
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