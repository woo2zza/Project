<template>
  <div class="main-container">
    <div class="main-top">
      <div class="main-top-content">
        <h1>Movie Signal</h1>
        <div class="custom-audio" ref="audioContainer">
          <div class="play-pause" @click="togglePlayPause">
            {{ isPlaying ? 'Pause' : 'Play' }}
          </div>
          <div class="progress" @click="seek" ref="progressContainer">
            <div class="progress-bar" :style="{ width: progress + '%', backgroundColor: 'rgba(79, 74, 133, 0.7)' }"></div>
          </div>
        </div>
      </div>
      <img src="../assets/아바타2.webp" alt="">
    </div>
    <div class="main-bottom">
      <MovieSlider />
      <TopRatedMovie />
      <WeatherRecommended />
    </div>
  </div>
</template>

<script setup>
import MovieSlider from "../components/MovieSlider.vue";
import TopRatedMovie from "@/components/TopRatedMovie.vue";
import WeatherRecommended from "@/components/WeatherRecommended.vue";
import { ref, onMounted } from 'vue';

const progressContainer = ref(null);
const progressInterval = ref(null);
const audioContainer = ref(null);
const audio = ref(new Audio('https://p.scdn.co/mp3-preview/8064eef0f1170380720c7c124eabf2d06b3f2170'));
const isPlaying = ref(false);
const progress = ref(0);

const togglePlayPause = () => {
  if (isPlaying.value) {
    audio.value.pause();
  } else {
    audio.value.play();
  }
  isPlaying.value = !isPlaying.value;
};

const updateProgress = () => {
  progress.value = (audio.value.currentTime / audio.value.duration) * 100;
};

const seek = (event) => {
  const clickedPosition = event.clientX - progressContainer.value.getBoundingClientRect().left;
  const totalWidth = progressContainer.value.offsetWidth;
  const seekTime = (clickedPosition / totalWidth) * audio.value.duration;
  audio.value.currentTime = seekTime;
};

onMounted(() => {
  audio.value.addEventListener('timeupdate', updateProgress);
  audio.value.addEventListener('play', () => {
    progressInterval.value = setInterval(updateProgress, 100);
  });
  audio.value.addEventListener('pause', () => {
    clearInterval(progressInterval.value);
  });
});
</script>



<style scoped>
.main-container {
  margin: 0;
  padding: 0;
}

.main-top {
  position: relative;
  width: 100%;
  overflow: hidden;
}

.main-top::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
}

.main-top-content {
  position: absolute;
  top: 90%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  color: white;
}

.main-top img {
  width: 100%;
  height: 700px;
  object-fit: cover;
}

.movie-slide {
  height: 330px;
  width: 100%;
}
.custom-audio {
  display: flex;
  align-items: center;
}

.play-pause {
  cursor: pointer;
  margin-right: 10px;
}

.progress {
  cursor: pointer;
  width: 100%;
  height: 10px;
  background-color: #ddd;
  position: relative;
}

.progress-bar {
  height: 100%;
  background-color: #4F4A85;
}

</style>
