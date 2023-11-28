<template>
    <div>
        <div class="carousel-item">
            <div class="row movie-item">
                <div class="col-md-6 col-sm-12">
                    <img :src='getImgUrl(topmovie.backdrop_path)' class="d-block w-100" alt="...">
                </div>
                <div class="col-md-6">
                    <div class="movie-item-content">
                        <h4 class="movie-title">{{ topmovie.title }}</h4>
                        <div class="overview-content">{{ topmovie.overview }}</div>
                        <hr>
                        <button
                            type="button"
                            class="btn btn-primary youtubebtn"
                            data-bs-toggle="modal"
                            data-bs-target="#youtubeTrailerModal"
                        >▶ 예고편
                        <img class="youtube" src="../assets/youtubeLogp.svg" alt="">
                        </button>
                        <YoutubeTrailerModal :movieTitle="topmovie.title" />    
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import YoutubeTrailerModal from './YoutubeTrailerModal.vue';
import { useRouter } from 'vue-router'
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores/movies'


const store = useMovieStore()
const router = useRouter()
const props = defineProps({
    topmovie:Object
})
const getImgUrl = (path) => {
  return `https://image.tmdb.org/t/p/w500${path}`;
};






</script>

<style scoped>
.movie-title {
    font-size: 1.9rem;
}
.movie-item{
    background-color: rgba(93, 18, 210, 0.5);
}
.movie-item-content{
    background-color: rgba(0, 0, 0, 0.131);
    border: 0.5px solid rgba(0, 0, 0, 0.131);
    height: 83%;
    width: 95%;
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

.youtubebtn {
    border: 0;
    background-color: rgb(244, 234, 224);
    color: black;
}

.youtube {
    height: 30px;
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