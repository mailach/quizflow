<template>
  <h1>Overview</h1>
    <v-container>
      <v-row justify="center">
        <v-col cols="12">
          <v-expansion-panels v-model="expandedPanel" variant="popout">
            <v-expansion-panel v-for="(questions, round) in groupedByRound" :key="round" class="exp-panel" >
              <v-expansion-panel-title>Round {{ round }}</v-expansion-panel-title>
              <v-expansion-panel-text>
                <v-list class="question-list">
                  <v-list-item v-for="question in questions" :key="question.id" class="question">
                    <!-- Directly place your content here -->
                    {{ question }}
                    <v-btn  @click="deleteQuestion(question)" class="add-btn">
                      <v-icon icon="fa-solid fa-trash" class="add-icon"></v-icon>
                    </v-btn> 
                  </v-list-item>
                </v-list>
              </v-expansion-panel-text>
              <!-- Button to open dialog -->
              <v-btn v-if="expandedPanel==round" @click="openCreateDialog(round)" class="add-btn">
                <v-icon icon="fa-solid fa-plus" class="add-icon"></v-icon>
              </v-btn>                
                <!-- Dialog for creating new question -->
                <v-dialog v-model="dialog" persistent max-width="600px" class="custom-dialog">
                        <v-btn icon class="dialog-close-btn" @click="dialog = false">
                          <v-icon icon="fa-solid fa-xmark"></v-icon>
                        </v-btn>
                <NewQuestion :round="selectedRound" :socket="socket" @close-dialog="dialog = false" />
                </v-dialog>
            </v-expansion-panel>
          </v-expansion-panels>

          <v-btn v-if="expandedPanel==round" @click="openCreateDialog(round)" class="add-btn">
            <v-icon icon="fa-solid fa-plus" class="add-icon"></v-icon>
          </v-btn>                
            <!-- Dialog for creating new question -->
            <v-dialog v-model="dialog" persistent max-width="600px" class="custom-dialog">
                    <v-btn icon class="dialog-close-btn" @click="dialog = false">
                      <v-icon icon="fa-solid fa-xmark"></v-icon>
                    </v-btn>
            <NewQuestion :round="selectedRound" :socket="socket" @close-dialog="dialog = false" />
            </v-dialog>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  

  <script setup>
  import { defineProps, computed, ref } from 'vue';
  import NewQuestion from '@/components/NewQuestion.vue';

  
  const props = defineProps({
    questions: {
      type: Array,
      required: true
    },
    socket: {
      type: Object,
      required: true
    }
  });
  const expandedPanel = ref(null); // Tracks the currently opened panel
    const dialog = ref(false);
    const selectedRound = ref(0);

    const openCreateDialog = (round) => {
    selectedRound.value = round;
    dialog.value = true;
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
    
    color: rgb(var(--v-theme-primary))
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