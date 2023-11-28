<template>
    <div v-if="store.topmovies">
    <h3 class="container-title">오늘의 영화 Top10</h3>
    <div id="carouselExampleAutoplaying" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
        <div class="carousel-item active movie-item">
            <div class="row">
                <div class="col-md-6 col-sm-12">
                    <img :src='getImgUrl(store.topmovies[0].backdrop_path)' class="d-block w-100" alt="...">
                </div>
                <div class="col-md-6">
                    <div class="movie-item-content">
                        <h4 class="movie-title">{{ store.topmovies[0].title }}</h4>
                        <div class="overview-content">{{ store.topmovies[0].overview }}</div>
                        <hr>
                        <button 
                            type="button"
                            class="btn btn-primary youtubebtn"
                            data-bs-toggle="modal"
                            data-bs-target="#youtubeTrailerModal"
                        >▶ 예고편
                        <img class="youtube" src="../assets/youtubeLogp.svg" alt="">
                        </button>
                        <YoutubeTrailerModal :movieTitle="store.topmovies[0].title" />  
                    </div>
                </div>
            </div>
        </div>
        <TopRatedMovieDetail
        v-for="topmovie in topmovies"
        :key="topmovie.id"
        :topmovie="topmovie"
        />
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleAutoplaying" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
    </button>
    </div>


    </div>
</template>

<script setup>

import 'animate.css';
import { onMounted, ref, computed } from 'vue'
import { useMovieStore } from '@/stores/movies'
import TopRatedMovieDetail from '@/components/TopRatedMovieDetail.vue'
import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue';
const store = useMovieStore()

const topmovies = computed(()=>{
    return store.topmovies.splice(1, 9)
})

onMounted(()=>{
    store.TopMovie()
})


const getImgUrl = (path) => {
  return `https://image.tmdb.org/t/p/w500${path}`;
};



</script>

<style scoped>


.container-title {
    
    font-style: italic;
    font-weight: 300;
    margin-top: 40px;
    margin-bottom: 10px;
    margin-left: 20px;
}

.movie-item{
    background-color: rgba(93, 18, 210, 0.5);
}
.movie-title {
    font-size: 1.9rem;
}

.movie-item-content{
    background-color: rgba(0, 0, 0, 0.131);
    border: 0.5px solid rgba(0, 0, 0, 0.131);
    height: 80%;
    width: 93%;
    margin-top: 5%;
    padding: 5%;
    border-radius: 8px;
    color: white;
}

.movie-item-content .overview-content {
    font-size: 1.3rem;
    color: rgb(192, 192, 192);
    max-width: calc(100% - 38px);
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

.youtube {
    height: 30px;
}

.youtubebtn {
    border: 0;
    background-color: rgb(244, 234, 224);
    color: black;
}

@media (max-width: 768px) {
  .movie-item-content {
    display: none !important;
  }
}

@media (max-width: 992px) {
    .overview-content {
    display: none !important;
  }
}

</style>