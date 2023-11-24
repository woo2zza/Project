<template>
  <div class="profile-page">
    <div v-if="store.profiles">
      <h3 class="page-title animate__animated animate__bounce">
        <span class="username">{{ store.profiles.username }}</span>님의 프로필
      </h3>
      <hr />



      <div class="follow">
        <div class="follow-button">
          <button
            v-if="gettoken.user.username != store.profiles.username"
            @click="toggleFollow"
            :class="{ follow: Following }"
            class="menu align-center expanded text-center SMN_effect-8"
            id="follow-button"
          >
            <p class="button-text">
              <a v-show="!Following" href="" data-hover="팔로우">
                <span><i class="fa-solid fa-people-arrows click"></i></span>
              </a>
              <a v-show="Following" href="" data-hover="언팔로우">
                <span><i class="fa-solid fa-people-arrows click"></i></span>
              </a>
            </p>
          </button>
        </div>

      <div class="container follow-container">
        <div class="row">
          <div class="col-sm-6 accordion accordion-flush follow-accordion" id="accordionFlushExample">
            <div class="accordion-item-left">
              <h2 class="accordion-header">
                <button class="accordion-button collapsed left" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
                  {{ store.profiles.username }}님을 추가한 이웃 ({{ store.profiles.follower_count }})
                </button>
              </h2>
              <div id="flush-collapseOne" class="accordion-collapse collapse" data-bs-parent="#accordionFlushExample">
                <div class="accordion-body">
                  <div class="comment-container list-group">
                    <FollowerList
                        class="list-group-item comment-list"
                        v-for="follower in store.profiles.followers"
                        :key="follower.id"
                        :follower="follower"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div
              class="col-sm-6 accordion accordion-flush"
              id="accordionFlushExample"
            >
              <div class="accordion-item-right">
                <h2 class="accordion-header">
                  <button
                    class="accordion-button collapsed right"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#follower"
                    aria-expanded="false"
                    aria-controls="follower"
                  >
                    {{ store.profiles.username }}님이 추가한 이웃 ({{
                      store.profiles.following_count
                    }})
                  </button>
                </h2>
                <div
                  id="follower"
                  class="accordion-collapse collapse"
                  data-bs-parent="#accordionFlushExample"
                >
                  <div class="accordion-body">
                    <div class="comment-container list-group">
                      <FollowerList
                        class="list-group-item comment-list"
                        v-for="follower in store.profiles.followings"
                        :key="follower.id"
                        :follower="follower"
                      />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <hr />
      <h3>{{ store.profiles.username }}님의 저장한 콘텐츠 목록</h3>
      <div v-if="IsEmpty_pick">
        <div class="d-flex flex-row" style="overflow-x: auto">
          <RecommendedDetail
            v-for="movie in store.profiles.like_movies"
            :key="movie.id"
            :movie="movie"/>
        </div>
      </div>
      <div v-else>
        <div class="save_content">
          <p>"영화를 더 편하게 즐기고 싶다면, '나만의 저장' 기능을 활용해보세요! 아직 저장한 콘텐츠가 없다면, 아래의 영화에서 마음에 드는 작품이나 추천받은 작품을 찾아보세요! 👀🎬"</p>
          <RouterLink :to="{ name : 'MovieListView' }"><h1><i class="fa-solid fa-arrow-pointer"></i></h1></RouterLink>
        </div>
      </div>
      

      <br>
      <h3>{{ store.profiles.username }}님이 작성한 리뷰</h3>
      <div v-if="IsEmpty_review">
        <div class="d-flex flex-row" style="overflow-x: auto">
          <ReviewCardDetail
          v-for="review in store.profiles.review_set"
          :key="review.id"
          :review="review"
          />
        </div>
      </div>
      <div v-else>
        <div class="save_review">
          <p>"커뮤니티에 여러분의 목소리를 더해보세요! 아직 글을 작성하지 않으셨다면, 여러분의 생각과 경험을 공유해보는 것은 어떨까요? 🌐✨"</p>
          <RouterLink :to="{ name : 'ReviewListView' }"><h1><i class="fa-solid fa-pen-nib" style="color: #b121c4;"></i></h1></RouterLink>
        </div>
        </div>
    </div>
  </div>
</template>

<script setup>

import { useAccountStore } from '@/stores/accounts'
import { useRoute, useRouter } from 'vue-router'
import { onMounted } from 'vue';
import axios from 'axios'
import { ref, computed } from 'vue'
import RecommendedDetail from '@/components/RecommendedDetail.vue'
import ReviewCardDetail from '@/components/ReviewCardDetail.vue'
import FollowerList from '@/components/FollowerList.vue'

const store = useAccountStore()
const route = useRoute()
const router = useRouter()




const t = localStorage.getItem("accounts");
const gettoken = JSON.parse(t);




const followusers = ref([])

const Following = computed(() => {
  if (store.userpk != null) {
    store.getprofile(route.params.id)
    followusers.value = store.profiles.followers.map(item => item.id)
  return followusers.value.some((userpk)=>userpk == store.userpk)
  }
})

const toggleFollow = () => {
  store.follow(route.params.id, gettoken.token);
  Following.value = !Following.value;
  router.push({name:'ProfileView', params:{id:store.profiles.id}})
};



const IsEmpty_review = computed(() => {
  if (store.profiles.review_set != null) {
    return store.profiles.review_set.length > 0 ? true : false
  }
})
const IsEmpty_pick = computed(() => {
  if (store.profiles.review_set != null) {
  return store.profiles.like_movies.length > 0 ? true : false
  }
})

onMounted(() => {
  store.getprofile(route.params.id)
  window.scrollTo(0, 0);
})
</script>

<style scoped>

* {
  font-family: 'Pretendard-Regular';
}
.profile-page {
  min-height: 100vh;
  max-width: 100%;
  margin: 0 15%;
  padding: 30px;
  padding-bottom: 100px;
}

.page-title {
  font-size: 3em;
  margin-bottom: 20px;
  text-align: center;
  color: rgb(104, 104, 104);
}

.username {
  color: rgb(151, 151, 151);
}

h4 {
  font-style: italic;
  font-weight: 300;
  margin: 15px 0;
}



.click {
  color: rgb(77, 31, 184);
}

.follow {
  display: flex;
  flex-direction: row;

}

.follow-button button {
  background: transparent;
  border: 0;
}

.button-text {
  color: white;
}

.button-text a {
  width: 170px;
}

.button-text:hover {
  color: red;
}




.menu a {
  color: rgba(255, 255, 255, 0.8);
  padding: 15px 25px;
  /**/
  position: relative;
  display: block;
  text-decoration: none;
  text-transform: uppercase;
}

.SMN_effect-8 {
  position: relative;
  z-index: 1;
  width: 150px;
}

.SMN_effect-8 a {
  overflow: hidden;
  margin: 0 15px;
  padding: 0;
}

.SMN_effect-8 a span {
  display: block;

  padding: 10px 20px;
  background: #181818;
  -webkit-transition: -webkit-transform 0.3s;
  -moz-transition: -moz-transform 0.3s;
  transition: transform 0.3s;
}

.SMN_effect-8 a:before {
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  padding: 10px 20px;
  width: 100%;
  height: 100%;
  background: #000000;
  color: #ffffff;
  content: attr(data-hover);
  -webkit-transition: -webkit-transform 0.3s;
  -moz-transition: -moz-transform 0.3s;
  transition: transform 0.3s;
  -webkit-transform: translateX(-25%);
}

.SMN_effect-8 a:hover span, .SMN_effect-8 a:focus span {
  -webkit-transform: translateX(100%);
  -moz-transform: translateX(100%);
  transform: translateX(100%);
}

.SMN_effect-8 a:hover:before, .SMN_effect-8 a:focus:before {
  -webkit-transform: translateX(0%);
  -moz-transform: translateX(0%);
  transform: translateX(0%);
}




.follow-container {
  padding: 0 0;
  margin-left: 20px;
  width: 70%;
  margin: 0 auto;
}

.row {
  width: 100%;
}

.accordion {
  padding: 0;
}

.accordion-header {
  background: transparent;
}

.accordion-button {
  font-size: 1.3rem;
}

.accordion-item-left {
  border-top-left-radius: 20px;
}

.accordion-item-right {
  border-top-right-radius: 20px;
}
.left {
  background-color: rgb(51, 9, 99);
  border-top-left-radius: 20px;
  color: rgb(167, 167, 167);
}
.right {
  background-color: rgb(51, 9, 99);
  border-top-right-radius: 20px;
  color: rgb(167, 167, 167);
}

.accordion-body {
  padding: 0;
}
.accordion-collapse {
  background-color: rgba(192, 192, 192, 0.507);
}

.save_content, 
.save_review { 
    margin: 30px 0;
    text-align: center;
    padding: 20px 70px;
    background-color: rgba(27, 27, 27, 0.583);
    border-radius: 15px;
    border: 0.1px solid ;
  }

  .save_content p,
  .save_review p {
    font-size: 1.4rem;
    color: #d8d4d4;
  }

  .save_content h1,
  .save_review h1 {
    font-size: 2em;
    color: #ed4040;
    cursor: pointer;
    margin-top: 35px;
  }

  .save_content h1 i,
  .save_review h1 i {
    font-size: 2em;
  }

.saveimg {
  width: 5rem;
  height: 5rem;
  background: url(https://assets.nflxext.com/ffe/siteui/acquisition/ourStory/fuji/desktop/download-icon.gif)
    center center no-repeat;
}
</style>
