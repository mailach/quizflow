<template>
  <v-container fluid class="new-round-container">
    <v-row justify="center">
      <v-col cols="12">
        <v-form @submit.prevent="submitRound">
          <v-row no-gutters>

            <!-- First Column -->
            <v-col cols="12" md="12">
              <v-text-field
                label="Quiz Round"
                v-model.number="round.id"
                class="q-input-field"
                type="number"
                required
                solo
                flat
              ></v-text-field>
              <v-text-field
                label="Title"
                v-model="round.title"
                class="q-input-field"
                required
                solo
                flat
              ></v-text-field>
              <v-select
                label="Active"
                :items=boolChoice
                item-text="option"
                item-value="index"
                v-model="round.active"
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
  import { defineProps } from 'vue';
  
  const emit = defineEmits(['close-dialog']);

  // Define props
  const props = defineProps({
    socket: {
      type: Object,
      required: true
    }
  });
  
  // Reactive state
  const round = ref({
    id: undefined,
    title: '',
    active: "",
  });
  
  const boolChoice = ref(["true", "false"])

  console.log(round.value)
  // Methods
  const submitRound = () => {
    console.log(round.value)
    props.socket.emit('create-round', round.value);
    console.log('Round submitted:', round.value);
    resetForm();
    emit('close-dialog');
  };

  
  const resetForm = () => {
    round.value = {
    id: '',
    text: '',
    active: "false",
    };
  };
  </script>
  
  <style scoped>
  .new-round-container {
    background: rgb(var(--v-theme-surface));
    border-radius: 20px;
  }
  
  .q-input-field {
    margin-right: 20px;
  }
  </style>