<template>
    <v-container>
      <v-row justify="center">
        <v-col cols="12">
          <h2>Existing Questions</h2>
          <v-expansion-panels v-model="expandedPanel" variant="popout">
            <v-expansion-panel v-for="(questions, round) in groupedByRound" :key="round" >
              <v-expansion-panel-title>Round {{ round }}</v-expansion-panel-title>
              <v-expansion-panel-text>
                <v-list>
                  <v-list-item v-for="question in questions" :key="question.id">
                    <!-- Directly place your content here -->
                    {{ question.text }} - Points: {{ question.points }}
                  </v-list-item>
                </v-list>
              </v-expansion-panel-text>
              <!-- Button to open dialog -->
              <v-btn v-if="expandedPanel==round" @click="openCreateDialog(round)">
                Create Question
              </v-btn>                
                <!-- Dialog for creating new question -->
                <v-dialog v-model="dialog" persistent max-width="600px" class="custom-dialog">
                        <v-btn icon class="dialog-close-btn" @click="dialog = false">
                          <v-icon>mdi-close</v-icon>
                        </v-btn>
                <NewQuestion :round="selectedRound" :socket="socket" @close-dialog="dialog = false" />
                </v-dialog>
            </v-expansion-panel>
          </v-expansion-panels>
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
  .custom-dialog .v-dialog__content {
    background: white;
  }

  .dialog-close-btn {
    position: absolute;
    top: 0;
    right: 0;
    z-index: 5; /* Ensure it's above other dialog content */
  }
</style>