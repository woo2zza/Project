<template>

    <div class="row">
      <div class="col-lg-2 left-container">
        <img class="poster-img1" :src="getImgUrl(movie.poster_path)" alt="">
      </div>
      <div class="col-lg-5 col-md-6 center-container">
        <h3>{{ movie.title }}</h3>
        <h3>{{ movie.original_title }}</h3>
        <p>{{ movie.release_date }}</p>
        <hr>
        <p class="overview-content">{{ movie.overview }}</p>
      </div>
      <div class="col-lg-5 col-md-6 right-container">
        <img class="poster-img2" :src="getImgUrl(movie.backdrop_path)" alt="">
      </div>
    </div>
</template>
  
<script setup>
const props = defineProps({
    movie:Object
})
const getImgUrl = (path) => {
  return `https://image.tmdb.org/t/p/w500${path}`;
};

</script>

<style scoped>
/* .row {
  height: auto;
} */

.poster-img1 {
  width: 100%;
  border-top-left-radius: 18px;
  border-bottom-left-radius: 18px;
}
.poster-img2{
  width: 100%;
  height: 100%;
  border-top-right-radius: 18px;
  border-bottom-right-radius: 18px;
}
.left-container {
  margin: 0;
  padding: 0;
}

.center-container {
  /* border: 0.5px solid whitesmoke; */

  padding: 30px 15px;
  background-color: rgba(255, 255, 255, 0.1);
}

.right-container {

  margin: 0;
  padding: 0;
}

.overview-content {
    max-width: calc(100% - 38px);
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

@media (max-width: 992px) {
  .overview-content {
    display: none !important;
  }
  .left-container {
    display: none !important;
  }
}
@media (max-width: 756px) {
  .right-container {
    display: none !important;
  }
}
</style>