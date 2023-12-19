<template>
    <v-container>
      <v-row>
        <v-col cols="12">
          <h2>Existing Questions</h2>
          <v-list>
            <v-list-item v-for="question in questions" :key="question.id">
              <!-- Use v-list-item-title for the text content -->
              <v-list-item-title>
                {{ question.text }} - Points: {{ question.points }}
              </v-list-item-title>
            </v-list-item>
          </v-list>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    name: 'QuestionList',
    props: {
      questions: {
        type: Array,
        required: true
      }
    }
  }
  </script>
  