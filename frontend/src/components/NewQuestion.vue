<template>
  <v-container fluid class="new-question-container">
    <v-row justify="center">
      <v-col cols="12">
        <v-form @submit.prevent="submitQuestion">
          <v-row no-gutters>

            <!-- First Column -->
            <v-col cols="12" md="6">
              <v-text-field
                label="Quiz Round"
                v-model.number="question.round"
                class="q-input-field"
                type="number"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Question ID"
                v-model="question.id"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Question Type"
                v-model="question.type"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Points"
                v-model.number="question.points"
                class="q-input-field"
                type="number"
                required
                solo
                flat
              ></v-text-field>
            </v-col>

            <!-- Second Column -->
            <v-col cols="12" md="6">
              <v-text-field
                label="Question Text"
                v-model="question.text"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Answer 1"
                v-model="question.options[0]"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Answer 2"
                v-model="question.options[1]"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Answer 3"
                v-model="question.options[2]"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Answer 4"
                v-model="question.options[3]"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-select
                label="Correct Answer"
                :items="options"
                item-text="option"
                item-value="index"
                v-model="question.correctAnswer"
                class="q-input-field"
                solo
                flat
              ></v-select>
            </v-col>

          </v-row>
          <v-btn type="submit" color="primary">Submit</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

  
  <script setup>
  import { ref } from 'vue';
  
  const emit = defineEmits(['close-dialog']);

  // Define props
  const props = defineProps({
    socket: {
      type: Object,
      required: true
    }
  });
  
  // Reactive state
  const question = ref({
    id: '',
    text: '',
    options: Array(4).fill(''),
    correctAnswer: 0,
    points: 0,
    type: 'multiple-choice',
    round: 0,
  });
  const options = ref([1, 2, 3, 4]);
  
  // Methods
  const submitQuestion = () => {
    console.log(question.value)
    props.socket.emit('create-question', question.value);
    console.log('Question submitted:', question.value);
    resetForm();
    emit('close-dialog');
  };

  
  const resetForm = () => {
    question.value = {
      id: '',
      text: '',
      options: Array(4).fill(''),
      correctAnswer: 0,
      points: 0,
      type: 'multiple-choice',
      round: 0,
    };
  };
  </script>
  
  <style scoped>
  .new-question-container {
    background: rgb(var(--v-theme-surface));
    border-radius: 20px;
  }
  
  .q-input-field {
    margin-right: 20px;
  }
  </style>