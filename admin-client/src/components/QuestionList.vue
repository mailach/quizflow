<template>
  <div class="text-h3">Overview</div>
    <v-container class="overview-box">
      <v-row justify="center" class="overview-box">
        <v-col cols="12" class="overview-box">
          <v-expansion-panels v-model="expandedPanel" variant="popout">
            <v-expansion-panel v-for="round in rounds" :key="round" class="exp-panel" >
              <v-expansion-panel-title>
                <div class="panel-title">
                <p>Round {{ round["id"] }}: {{round["title"]}} </p>
                <div class="panel-icons">
                  <v-btn icon @click="openRoundDialog(round)" class="play-btn">
                    <v-icon icon="fa-solid fa-gear" class="play-icon"></v-icon>
                  </v-btn> 
                <v-btn icon @click="console.log('Play')" class="play-btn">
                  <v-icon icon="fa-solid fa-play" class="play-icon"></v-icon>
                </v-btn>  
                <v-btn icon @click="console.log('Delete')" class="play-btn">
                  <v-icon icon="fa-solid fa-trash" class="play-icon"></v-icon>
                </v-btn> 
              </div>
            </div>
              </v-expansion-panel-title>
              <v-expansion-panel-text>
                <v-list class="question-list">
                  <v-list-item v-for="question in groupedByRound[round['id']]" :key="question.id" class="question">
                    <!-- Directly place your content here -->
                    {{ question }}
                    <v-btn  @click="deleteQuestion(question)" class="add-btn">
                      <v-icon icon="fa-solid fa-trash" class="add-icon"></v-icon>
                    </v-btn> 
                  </v-list-item>
                </v-list>
                <v-btn @click="openQuestionDialog(round)" class="add-btn">
                  <v-icon icon="fa-solid fa-plus" class="add-icon"></v-icon> <p>Question</p>
                </v-btn> 
              </v-expansion-panel-text>
              <!-- Button to open dialog -->
                             
                <!-- Dialog for creating new question -->
                
            </v-expansion-panel>
          </v-expansion-panels>
            <v-btn @click="openRoundDialog({id: '', title:'', active:''})" class="add-btn">
              <v-icon icon="fa-solid fa-plus" class="add-icon"></v-icon><p>Round</p>
            </v-btn>                
              <!-- Dialog for creating new question -->


              <v-dialog v-model="questionDialog" persistent max-width="600px" class="custom-dialog">
                <v-btn icon class="dialog-close-btn" @click="questionDialog = false">
                  <v-icon icon="fa-solid fa-xmark"></v-icon>
                </v-btn>
              <NewQuestion :round="selectedRound" :socket="socket" @close-dialog="questionDialog = false" />
              </v-dialog>

              <v-dialog v-model="roundDialog" persistent max-width="600px" class="custom-dialog">
                      <v-btn icon class="dialog-close-btn" @click="roundDialog = false">
                        <v-icon icon="fa-solid fa-xmark"></v-icon>
                      </v-btn>
              
              <NewRound :originRound="round" :socket="socket" @close-dialog="roundDialog = false" />
              </v-dialog>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  

  <script setup>
  import { defineProps, computed, ref } from 'vue';
  import NewQuestion from '@/components/NewQuestion.vue';
  import NewRound from '@/components/NewRound.vue';

  
  const props = defineProps({
    questions: {
      type: Array,
      required: true
    },
    rounds: {
      type: Array,
      required: true
    },
    socket: {
      type: Object,
      required: true
    }
  });
  const expandedPanel = ref(null); // Tracks the currently opened panel
    const questionDialog = ref(false);
    const roundDialog = ref(false);
    const selectedRound = ref(0);
    let round = ref({id: '', title:'', active:''});

    const openQuestionDialog = (round) => {
    selectedRound.value = round;
    questionDialog.value = true;
    };

    const openRoundDialog = (selectedRound) => {
    roundDialog.value = true;
    round.value = selectedRound
    };

    const deleteQuestion = (question) => {
    props.socket.emit('delete-question', question);
    };



  const groupedByRound = computed(() => {
    const rounds = {};
  
    props.questions.forEach(question => {
      if (!rounds[question.round]) {
        rounds[question.round] = [];
      }
      rounds[question.round].push(question);
    });
  
    return rounds;
  });
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
</style>