<template>
    <div class="">
      <h3 class="container-title">오늘 날씨는 {{ todayWeather }}! 이 영화는 어떠세요?</h3>
      <div class="recommend-container" v-if="recommendedMovie">
        <WeatherRecommendedDetail :movie="recommendedMovie"/>
      </div>
    </div>
  </template>
  
  <script setup>
  import WeatherRecommendedDetail from '@/components/WeatherRecommendedDetail.vue';
  import axios from 'axios';
  import { ref, onMounted } from 'vue'
  const weatherApiKey = import.meta.env.VITE_WEATHER_API_KEY;
  const key = import.meta.env.VITE_TMDB_API_KEY
  
  const recommendedMovie = ref(null)
  const weatherStatus = ref('')
  const todayWeather = ref('')
  
  const fetchWeather = () => {
    const URL = `http://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=${weatherApiKey}`;
    axios.get(URL)
      .then((response) => {
        weatherStatus.value = response.data.weather[0].main
        selectGenreByWeather(weatherStatus.value)
      })
      .catch((error)=>{
        console.log(error)
      })
  }
  const selectGenreByWeather = (weatherStatus) => {
    switch (weatherStatus) {
      case 'Rain':
        todayWeather.value='비가 와요'
        return 27
      case 'Snow':
        todayWeather.value='눈이 와요'
        return 10749
      case 'Clear':
        todayWeather.value='맑아요'
        return 12
      case 'Clouds':
        todayWeather.value='흐려요'
        return 35
      default:
        todayWeather.value=' '
        return 35
    }
  }
  
  const fetchMovie = () => {
    const genre = selectGenreByWeather(weatherStatus.value)
  
    const URL = `https://api.themoviedb.org/3/discover/movie?with_genres=${genre}&language=ko-KR&page=1`;
    const headers = {
      accept: "application/json",
      Authorization: `Bearer ${key}`,
    };
    axios.get(URL, { headers })
    .then((response) => {
      const movies = response.data.results.slice(0, 100)
      recommendedMovie.value = movies[Math.floor(Math.random() * movies.length)]
    })
    .catch((error)=>{
      console.log(error)
    })
  }
  
  
  onMounted(fetchWeather);
  onMounted(fetchMovie);
  
  
  
  </script>
  
<style scoped>
.container-title {
    font-style: italic;
    font-weight: 300;
    margin-top: 40px;
    margin-bottom: 10px;
    margin-left: 20px;
}

.recommend-container{
  background-image: linear-gradient(to right bottom, #20003d, #251040, #2b1d43, #322944, #393545, #3b3845, #3e3c44, #403f44, #3e3b44, #3c3744, #3a3244, #392e43);
  padding: 3%;
}
</style>