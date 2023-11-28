<template>
  <div class="top">
    <figure class="snip1368">
      <img
        class="poster-img"
        :src="getImgUrl(review.movie.poster_path)"
        alt=""
        @click="goDetail"
      />
      <h3>{{ review.movie.title }}</h3>
      <figcaption>
        <i class="fa-regular fa-comment-dots icon"></i>
          <p class="commentcnt">{{ review.commentcount }}개의 댓글이 달렸어요!</p>
      </figcaption>
    </figure>
  </div>
</template>

<script setup>
import { useRouter } from "vue-router";
import { useReviewCommentStore } from "@/stores/reviewcomments"
const store = useReviewCommentStore
const router = useRouter();
const props = defineProps({
  review: Object,
});

const getImgUrl = (path) => {
  return `https://image.tmdb.org/t/p/w500${path}`;
};




const goDetail = function () {
  router.push({ name: "ReviewDetailView", params: { id: props.review.id } });
};

    </script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=Roboto:300,400);
@import url(https://code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css);

  figure.snip1368 {
  font-family: 'Roboto', Arial, sans-serif;
  position: relative;
  overflow: hidden;
  margin: 30px 5px;
  min-width: 230px;
  max-width: 315px;
  width: 100%;
  color: #ffffff;
  line-height: 1.4em;
}
figure.snip1368 * {
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: all 0.4s ease;
}
figure.snip1368 img {
  opacity: 1;
  width: 100%;
  height: 350px;
  object-fit: cover;
  object-position: center;
  vertical-align: top;
}
figure.snip1368 h3 {
  position: absolute;
  top: 0%;
  width: 100%;
  background-color: #212121;
  z-index: 1;
  text-align: right;
  padding: 15px 25px 0px;
  margin: 0;
  font-weight: 300;
  font-size: 1.2em;
  -webkit-transform: translateY(-200%);
  transform: translateY(-200%);
}
figure.snip1368 h3:before {
  position: absolute;
  content: '';
  top: 100%;
  left: 0;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 0 315px 55px 0;
  border-color: transparent #212121 transparent transparent;
}
figure.snip1368 figcaption {
  padding: 5px 25px 15px;
  position: absolute;
  width: 100%;
  z-index: 2;
  bottom: -5%;
  background-color: #141414;
  -webkit-transform: translateY(200%);
  transform: translateY(200%);
}
figure.snip1368 figcaption:before {
  position: absolute;
  content: '';
  bottom: 100%;
  left: 0;
  width: 0;
  height: 0;
  border-style: solid;
  border-width: 55px 0 0 315px;
  border-color: transparent transparent transparent #141414;
}
figure.snip1368 .icons {
  margin-top: -20px;
}
figure.snip1368 i {
  padding: 0px 8px;
  display: inline-block;
  font-size: 24px;
  color: #ffffff;
  text-align: center;
  opacity: 0.7;
}

figure.snip1368:hover h3,
figure.snip1368.hover h3 {
  -webkit-transform: translateY(0%);
  transform: translateY(0%);
}
figure.snip1368:hover figcaption,
figure.snip1368.hover figcaption {
  -webkit-transform: translateY(0%);
  transform: translateY(0%);
}

.snip1368:hover {
  scale: 1.1;
  z-index: 0.5;
}
</style>
