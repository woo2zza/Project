<template>
  <figure class="snip1432">
    <div class="card" >
      <img
        class="poster-img"
        :src="getImgUrl(movie.poster_path)"
        alt=""
        @click="goDetail"
      />
      <figcaption>
        <div>
          <h3></h3>
          <h3 class="title" @click="goDetail">{{ movie.title }}</h3>
        </div>
        
      </figcaption>
    </div>
  </figure>
</template>

<script setup>
import { useRouter } from "vue-router";
const router = useRouter();
const props = defineProps({
  movie: Object,
});

const getImgUrl = (path) => {
  return `https://image.tmdb.org/t/p/w500${path}`;
};

const goDetail = function () {
  router.push({ name: "MovieDetailView", params: { id: props.movie.id } });
};
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Raleway:500,900);
figure.snip1432 {
  margin: 30px 5px;
  width: 230;
  min-width: 230px;
  max-width: 243px;
  width: 100%;
  color: #ffffff;
}
figure.snip1432 * {
  -webkit-transition: all 0.6s ease;
  transition: all 0.6s ease;
}
figure.snip1432 img {
  width: 100%;
  height: 350px;
  vertical-align: top;
  -webkit-transition: opacity 0.35s;
  transition: opacity 0.35s;
}
figure.snip1432 figcaption {
  position: absolute;
  width: 100%;
  height: 100%;
}
figure.snip1432 figcaption > div {
  height: 50%;
  overflow: hidden;
  width: 100%;
  position: relative;
}

figure.snip1432 h3 {
  margin: 0;
  position: absolute;
  left: 0;
  padding: 0 30px;
  text-transform: uppercase;
}

figure.snip1432 h3 {
  font-size: 1.2rem;
  bottom: 0;
  font-weight: 500;
}
figure.snip1432 h3:nth-of-type(2) {
  opacity: 0;
  -webkit-transform: translateY(150%);
  transform: translateY(150%);
}

figure.snip1432:hover img,
figure.snip1432.hover img {
  opacity: 0.3;
  -webkit-filter: grayscale(100%);
  filter: grayscale(100%);
}

figure.snip1432:hover figcaption h3:nth-of-type(2),
figure.snip1432.hover figcaption h3:nth-of-type(2) {
  opacity: 1;
  -webkit-transform: translateY(0%);
  transform: translateY(0%);
}
.card {
  background: 0;
  font-size: 15px;
  color: white;
}

.card:hover {
  scale: 1.1;
  z-index: 0.5;
}
</style>
