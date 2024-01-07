<template>
  <h1>Overview</h1>
    <v-container>
      <v-row justify="center">
        <v-col cols="12">
          <v-expansion-panels v-model="expandedPanel" variant="popout">
            <v-expansion-panel v-for="round in rounds" :key="round" class="exp-panel" >
              <v-expansion-panel-title>Round {{ round }}</v-expansion-panel-title>
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
                <v-dialog v-model="questionDialog" persistent max-width="600px" class="custom-dialog">
                        <v-btn icon class="dialog-close-btn" @click="questionDialog = false">
                          <v-icon icon="fa-solid fa-xmark"></v-icon>
                        </v-btn>
                <NewQuestion :round="selectedRound" :socket="socket" @close-dialog="questionDialog = false" />
                </v-dialog>


                
            </v-expansion-panel>
          </v-expansion-panels>
            <v-btn @click="openRoundDialog()" class="add-btn">
              <v-icon icon="fa-solid fa-plus" class="add-icon"></v-icon><p>Round</p>
            </v-btn>                
              <!-- Dialog for creating new question -->
              <v-dialog v-model="roundDialog" persistent max-width="600px" class="custom-dialog">
                      <v-btn icon class="dialog-close-btn" @click="roundDialog = false">
                        <v-icon icon="fa-solid fa-xmark"></v-icon>
                      </v-btn>
              <NewRound :socket="socket" @close-dialog="roundDialog = false" />
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
    const round = ref(undefined);

    const openQuestionDialog = (round) => {
    selectedRound.value = round;
    questionDialog.value = true;
    };

    const openRoundDialog = () => {
    roundDialog.value = true;
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

  .add-btn{
    
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around

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
</style>