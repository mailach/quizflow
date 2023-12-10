<template>
    <component :is="component" :msg="questionData.msg" :choices="questionData.choices"></component>
  </template>
  
  <script setup lang="ts">
  import {computed } from 'vue';
  import MultipleChoiceQ from './MultipleChoiceQ.vue';
  import OpenQ from './OpenQ.vue';
  
  const props = defineProps<{ questionData: { type: string, msg: string, choices?: Array<string> } }>();
  
  const component = computed(() => {
    return props.questionData.type === 'multiple-choice' ? MultipleChoiceQ : OpenQ;
  });
  </script>
  
  <style>
  /* Add any styles specific to this component here */
  </style>
  