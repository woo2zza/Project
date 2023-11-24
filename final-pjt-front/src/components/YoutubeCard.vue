<template>
  <div class="youtube-card" @click="handleClick">
    <img :src="thumbnail" alt="YouTube Video Thumbnail" />
    <div class="content-wrapper">
      <h5 v-html="title"></h5>
      <div class="youtube-description"># {{ descriptions }}</div>
    </div>
  </div>
</template>

<script setup>
import {} from 'vue'

const props = defineProps(['thumbnail', 'title', 'descriptions'])

const emit = defineEmits()

const handleClick = () => {
  emit('click')
}
</script>

<style scoped>
.youtube-card {
  display: flex;
  flex-direction: row;
  align-items: start;
  border: 0.3px solid #ccc;
  padding: 20px;
  cursor: pointer;
  margin-top: 1rem;
  border-radius: 8px;
  background-color: rgba(0, 0, 0, 0.407);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.youtube-card img {
  width: 200px;
  height: auto;
  border-radius: 4px;
}
.content-wrapper {
  margin-left: 1rem;
  flex-grow: 1;
}
.youtube-card h3 {
  margin-top: 0;
  font-size: 1.5em;
}
.youtube-description {
  font-size: 0.9em;
  margin-top: 0.5rem;
  color: rgb(119, 119, 119);
}
</style>
