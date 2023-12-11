<template>
  <div class="detail-page" v-if="store.movie">
    <div class="container">
      <div class="row">
        <div class="col-md-6">
          <img class="poster-img" :src="store.movie.poster_path" alt="" />
        </div>
        <div class="col-md-6">
          <h2>{{ store.movie.title }}
            <i class="fa-solid fa-check" :class="{ 'check': isLiked, 'uncheck': !isLiked }"></i>
          </h2>
          <p>개봉일: {{ store.movie.release_date }}</p>
          <p>평점 : {{ store.movie.vote_average }}</p>
          <p><span v-for="genre in store.movie.genres" :key="genre.name"> #{{ genre.name }} </span></p>
          <div v-show="store.movie.overview">
          <hr/>
            <p>{{ store.movie.overview }}</p>
          </div>
          <hr/>
          <div>
            <div class="movie-youtube">
              <span>▶️ 예고편 보기</span>
              <button
                type="button"
                class="youtube-btn"
                @click="openModal"
                data-bs-toggle="modal"
                data-bs-target="#youtubeTrailerModal"
              >
                <img :src="youtubeLogp" alt="YouTube" class="youtube-logo" />
              </button>
            </div>
            <YoutubeTrailerModal :movieTitle="store.movie.title" />
          </div>

          <div class="like" v-if="store.movie.like_users">
            <span>찜한 사람 : {{ store.movie.like_user_count }}</span

            ><br/>

            <button v-if="isLiked" @click="accountStore.isLogin? toggleLike() :goLogin()">
              <i class="fa-solid fa-download click"></i>
            </button>
            <button v-else @click="accountStore.isLogin? toggleLike() :goLogin()">
              <i class="fa-solid fa-download"></i>
            </button>
          </div>
        </div>
      </div>
    </div>

    <hr />
    <div class="comment-container list-group">
      <CommentCreate v-show="accountStore.isLogin" class="list-group-item create" :movieId="store.movie.id" />
      <CommentList
        class="list-group-item comment-list"
        v-for="comment in store.movie.moviecomment_set"
        :key="comment.id"
        :comment="comment"
      />
    </div>
    <div v-if="store.movie.genres">
      <Recommended :genres="store.movie.genres" />
    </div>
    <hr>

    <div v-if="review">
        <h3 class="container-title">작성된 리뷰 (<span>{{ store.movie.review_count }}</span>)</h3>
        <p class="d-inline-flex gap-1">
            <button class="btn" type="button" data-bs-toggle="collapse" data-bs-target="#review" aria-expanded="false" aria-controls="review">
            더보기
            </button>
        </p>
        <div class="collapse" id="review">
            <div class="d-flex flex-row" style="overflow-x:auto;">
                <MovieReviewCard
                    v-for="review in store.movie.review_set"
                    :key="review.id"
                    :review="review"/>
            </div>
        </div>
    </div>

    <div v-if="!review">
      <h3>아직 작성된 리뷰가 없어요, 리뷰를 작성해보세요!
        <i class="fa-solid fa-pencil click" @click="accountStore.isLogin? goReviewCreate() :goLogin()"></i>
      </h3>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movies";
import { useAccountStore } from "@/stores/accounts";
import { onMounted, ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import CommentCreate from "@/components/CommentCreate.vue";
import CommentList from "@/components/CommentList.vue";
import Recommended from "@/components/Recommended.vue";
import MovieReviewCard from "@/components/MovieReviewCard.vue"
import youtubeLogp from "@/assets/youtubeLogp.svg";
import YoutubeTrailerModal from "@/components/YoutubeTrailerModal.vue";

const store = useMovieStore();
const accountStore = useAccountStore();
const route = useRoute();
const type = ref(false);
const router = useRouter()


const likeusers = ref([])

const isLiked = computed(() => {
  if (store.movie.like_users != null && accountStore.userpk != null) {
    likeusers.value = store.movie.like_users.map(item => item.pk)
  return likeusers.value.some((userpk)=>userpk == accountStore.userpk)
  }
})

const review = computed(()=>{
  if (store.movie.review_set != null) {
    return store.movie.review_set.length > 0 ? true : false
  }
})

const goLogin=()=>{
  router.push({name:'LoginView'})
}

const goReviewCreate=()=>{
  router.push({name:'ReviewCreateView'})
}


const toggleLike = () => {
  store.likeMovie(store.movie.id);
  isLiked.value = !isLiked.value
  router.push({name:'MovieDetailView', params:{id:store.movie.id}})
};

onMounted(() => {
  store.getMovieDetail(route.params.id);
  if (accountStore.isLogin) {
    accountStore.getuser(accountStore.token)
  }
  window.scrollTo(0, 0);
})
</script>

<style scoped>
.detail-page {
  padding: 5rem 10%;
  color: white;
}

.liked {
  color: white;
}
.poster-img {
  width: 100%;
  border-radius: 10px;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.youtube-logo {
  width: 40px;
}
.youtube-btn {
  background: transparent;
  border: 0;
}
.comment-container {
  width: 100%;
  margin: 0;
}
.list-group-item {
  height: 45px;
  width: 100%;
}
.create {
  padding: 0;
  background: transparent;
  border: 0;
}
.comment-list {
  background-color: rgba(255, 255, 255, 0.459);
  border: 0;
  border-bottom: 0.5px solid black;
}

.click {
  color: gold;
}

.like button {
  background: transparent;
  border: 0;
  font-size: 40px;
}
.container button:hover {
  scale: 1.1;
}

.fa-check {
  color: #ffea00;
}

.uncheck {
  display: none;
}


.btn {
  color: white;
  background-color: rgba(96, 61, 116, 0.548);
}

.fa-pencil:hover {
  scale: 1.1;
  color: rgb(20, 122, 180);
}

</style>
