<template>
  <div class="gif-container">
    <img :src="gifUrl" alt="Displayed GIF" />
  </div>
</template>

<script>
console.log("TEST")
export default {
  props: {
    gifUrl: {
      type: String,
      required: true
    }
  }
}
</script>

<style>
.gif-container img {
  max-width: 100%;
  height: auto;
  display: block; /* Ensures the image does not have extra space below */
  margin: 0 auto; /* Centers the image if it's smaller than the container */
}
</style>
