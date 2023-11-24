<template>
  <figure class="card_all">
    <img @click="goDetail" :src="`https://image.tmdb.org/t/p/w500/${movie.poster_path}`" alt="Movie Poster" class="card-img-top">
    <figcaption>
    <div class="card_body">
      <p></p>
      <div class="title">{{ movie.title }}
        <i class="fa-solid fa-check" :class="{ 'click': isLiked, '': !isLiked }"></i>
      </div>
      <hr>
      <p class="text un">{{ movie.release_date }}</p>
      <p class="avg un">평점★ {{ movie.vote_average }}</p>
      <p class="gen un"><span v-for="genre in movie.genres"> #{{ genre.name }}</span></p>
    </div>
  </figcaption>
  </figure>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { onMounted,  computed, ref } from 'vue';
import { useMovieStore } from '@/stores/movies'
import { useAccountStore } from '../stores/accounts';
const store = useMovieStore()
const accountStore = useAccountStore()
const props = defineProps({
    movie:Object
})

const router = useRouter()
const goDetail = function () {
  router.push({name:'MovieDetailView', params:{id:props.movie.id}})
}

const likeusers = ref([])
const isLiked = computed(() => {
  if (props.movie.like_users != null && accountStore.userpk != null) {
    likeusers.value = props.movie.like_users.map(item => item.pk)
  return props.movie.like_users.some((userpk)=>userpk == accountStore.userpk)
  }
})


</script>

<style scoped>
  @import url(https://fonts.googleapis.com/css?family=Raleway:400,500,800);
.card_all {
  margin: 60px 15px;
  border: 1px solid rgb(137, 137, 137);
  border-radius: 5px;
  width: 200px;
  /* background-color: rgba(93, 18, 210, 0.5); */
}

.card_all:hover {
  scale: 1.05;
  z-index: 0.5;
}

.title {
  padding: 4px 0;
  background-color: rgba(0, 0, 0, 0.624);
}

figure.card_all {
  font-family: "Raleway", Arial, sans-serif;
  position: relative;
  overflow: hidden;
  margin: 30px;
  min-width: 100px;
  max-width: 210px;
  max-height: 450px;
  width: 100%;
  background: #000000;
  color: #ffffff;
  text-align: center;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.15);
  font-size: 16px;
}

figure.card_all * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.45s ease-in-out;
  transition: all 0.45s ease-in-out;
}

figure.card_all figcaption {
  position: absolute;
  top: 80%;
  left: 9.5%;
  right: 9.5%;
  bottom: 50%;
  border: 1px solid #5F00FF;
  border-width: 2px 2px 0;
}

figure.card_all p {
  top: 50%;
  transform: translateY(-80%);
  position: absolute;
  width: 100%;
  padding: 0 20px;
  margin: 0;
  opacity: 0;
  line-height: 1.6em;
  /* font-size: 2em; */
}

figure.card_all:hover img,
figure.card_all.hover img {
  opacity: 0.25;
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
figure.card_all:hover figcaption,
figure.card_all.hover figcaption {
  top: 20%;
  bottom: 15%;
}
figure.card_all:hover p.avg,
figure.card_all.hover p.avg {
  transform: translateY(-35px);
  opacity: 1;
  -webkit-transition-delay: 0.55s;
  transition-delay: 0.55s;
}
figure.card_all:hover p.text,
figure.card_all.hover p.text {
  transform: translateY(-5px);
  opacity: 1;
  -webkit-transition-delay: 0.35s;
  transition-delay: 0.35s;
}
figure.card_all:hover p.gen,
figure.card_all.hover p.gen {
  transform: translateY(25px);
  opacity: 1;
  -webkit-transition-delay: 0.35s;
  transition-delay: 0.35s;
}

figure.card_all .card_body hr {
  width: 100%;
  margin-top: 5px;
  margin-bottom: 10px;
  border: 2px solid #5F00FF;
}

.click {
  color: gold;
}
</style>