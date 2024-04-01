<template>
  <div class="text-h3">Teams</div>
    <v-container class="overview-box">
      <v-row justify="center" class="overview-box">
        <v-col cols="12" class="overview-box">
          <v-expansion-panels v-model="expandedPanel" variant="popout">
            <v-expansion-panel v-for="team in teams" :key="team" class="exp-panel" >
              <v-expansion-panel-title>
                <div class="panel-title">
                <p>Name: {{ team["id"] }} | Points: {{ team["points"]}} | Activated: {{team["activated"]}}</p>
                <div class="panel-icons">
                <v-btn icon @click="acceptTeam(team)" class="play-btn">
                  <v-icon icon="fa-solid fa-circle-check" class="play-icon"></v-icon>
                </v-btn>  
              </div>
            </div>
              </v-expansion-panel-title>
              <v-expansion-panel-text >                
                  <div>Team Infos</div>
              </v-expansion-panel-text>
              <!-- Button to open dialog -->
                             
                <!-- Dialog for creating new question -->
                
            </v-expansion-panel>
          </v-expansion-panels>
          </v-col>
      </v-row>
    </v-container>
  </template>
  
  

  <script setup>
    import {ref } from 'vue';

  
  const props = defineProps({
    teams: {
      type: Array,
      required: true
    },
    socket: {
      type: Object,
      required: true
    }
  });
  const expandedPanel = ref(null); // Tracks the currently opened panel

  const acceptTeam = (selectedTeam) => {
    console.log(selectedTeam)
    props.socket.emit('activate-team', selectedTeam)
    };

  </script>
  <style scoped>


  .question-list{
    min-width: 100%;
  }

  .add-icon{
    color: rgb(var(--v-theme-primary));
  }

  .play-icon{
    color: rgb(var(--v-theme-primary));
  }

  .add-btn{
    max-width: 100px;
    margin: 10px;
  }

  .play-btn{
    background-color: transparent;
    box-shadow: none;
  }
  .play-btn::before {
  background-color: transparent !important;
  }
  .play-btn::after {
    background-color: transparent !important;
  }


  .dialog-close-btn {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 5; /* Ensure it's above other dialog content */
  }

  .question{
    min-width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
  }
  .exp-panel{
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .overview-box {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
  }

  .text-h3 {
    align-items: center;
    text-align: center;
  }

  .panel-title {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 95%;
    align-items: center;
  }
  .panel-icons {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 18%;
    align-items: center;
  }

  .question-block-in-panel{
    display: flex;
    flex-direction: column;
    align-items: center;
  }

</style>