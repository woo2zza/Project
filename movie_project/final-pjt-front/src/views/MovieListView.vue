<template>
    <div class="list-page">
    <h1 class="page-title animate__animated animate__bounce">Movie List</h1>
    <hr>

    <div class="search-container">
        <input class="search-input" v-model="title" placeholder="영화 제목을 검색해보세요!" />
        <i class="fa-solid fa-magnifying-glass"></i>
    </div>
    <hr>
        <div class="list">
            <MovieListItem
                v-for="movie in filteredMovies"
                :key="movie.id"
                :movie="movie"
            />
        </div>


        <div class="list">
            <MovieListItem
                v-for="movie in movieStore.movies"
                :key="movie.id"
                :movie="movie"
            />
        </div>
    </div>
</template>


<script setup>
import { useMovieStore } from '@/stores/movies'
import MovieListItem from '@/components/MovieListItem.vue';
import { onMounted, ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import router from '../router';

const title = ref('')

const movieStore = useMovieStore()
const filteredMovies = computed(() => {
  const searchTerm = title.value.toLowerCase().trim();
  if (!searchTerm) {
    return movieStore.movies
  } else {
    return movieStore.movies.filter(movie =>
      movie.title.toLowerCase().trim().includes(searchTerm)
    );
  }
});

onMounted(() => {
    movieStore.getMovieList()
    window.scrollTo(0, 0);
})


</script>

<style scoped>
.list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    max-width: 1700px;
    margin: 0 auto;
    padding: 20px;
    text-align: center;
}

.list-page {
  min-height: 100vh;
  max-width: 100%;
  margin: 0 10%;
  padding: 30px;
  padding-bottom: 100px;
    }

.page-title {
  font-size: 3em;
  margin-bottom: 20px;
  text-align: center;
  color: rgb(104, 104, 104);
}

.search-container {
    display: flex;
    justify-content: flex-end;
}

.search-input {
    background-color: rgba(255, 255, 255, 0.26);
    border: 0;
    border-radius: 20px;
    padding: 0.3rem 0.7rem;
    width: 40%;
}

.search-input::placeholder {
    color: rgb(204, 204, 204);
    font-weight: 100;
    font-style: italic;
}
.search-input:focus {
    background-color: rgba(255, 255, 255, 0.466);
    outline: none;
}

.search-input:focus::placeholder {
    color: transparent;
}


.search-container {
  position: relative;
}

.search-label {
  display: flex;
  align-items: center;
}

.search-input {
  padding-right: 30px;
}

.fa-magnifying-glass {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
}
</style>