<template>
    <div v-if="recommendedMovie">
        <hr>
        <h3 class="container-title">비슷한 작품</h3>
        <p class="d-inline-flex gap-1">
            <button @click="fetchMovie" class="btn" type="button" data-bs-toggle="collapse" data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
            더보기
            </button>
        </p>
        <div class="collapse" id="collapseExample">

            <div class="d-flex flex-row" style="overflow-x:auto;">
                <RecommendedDetail
                    v-for="movie in recommendedMovie"
                    :key="movie.id"
                    :movie="movie"/>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { onMounted } from 'vue';
import axios from 'axios'
import RecommendedDetail from '@/components/RecommendedDetail.vue'

const props = defineProps({
    genres:Array
})
const key = import.meta.env.VITE_TMDB_API_KEY
const recommendedMovie = ref(null)

const fetchMovie = () => {
  const genre = props.genres[0]

  const URL = `https://api.themoviedb.org/3/discover/movie?with_genres=${genre}&language=ko-KR&page=1`;
  const headers = {
    accept: "application/json",
    Authorization: `Bearer ${key}`,
  };
  axios.get(URL, { headers })
  .then((response) => {
    const movies = response.data.results.slice(0, 15)
    recommendedMovie.value = movies
  })
  .catch((error)=>{
    console.log(error)
  })
}

onMounted(fetchMovie)


</script>

<style scoped>
.btn {
  color: white;
  background-color: rgba(96, 61, 116, 0.548);
}

</style>