<template>
  <div>
    <h2>Existing Questions</h2>
    <ul>
      <li v-for="question in questions" :key="question.id">
        {{ question.text }} - Points: {{ question.points }}
      </li>
    </ul>
  </div>
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
