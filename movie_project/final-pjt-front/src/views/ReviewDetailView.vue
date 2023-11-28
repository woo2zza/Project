<template>
    <div class="review-container" v-if="store.review.movie">

    <div class="back color-5">
    <div class="row columns">
      <div class="menu align-center expanded text-center SMN_effect-5">
        <div>
          <a>
            <h2>{{ store.review.movie.title }}</h2>
            <span 
             class="goDetail"
             @click="router.push({name:'MovieDetailView', params:{id:store.review.movie.id}})">
             영화 상세 정보</span>
          </a>
        </div>
      </div>
    </div>
    </div>


      <hr>
      <h3>{{ store.review.title }}</h3>
      <div>{{ store.review.content }}</div>
      <hr>
      <div class="userInfo">


        <p style="font-size: 20px;">글쓴이: {{ store.review.user.username }}
          <svg @click="goProfile" xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-house-fill mb-1" viewBox="0 0 16 16">
            <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"/>
            <path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z"/>
          </svg>
        </p>
        <p>{{ formattedDate }}</p>
        <button class="update-button" v-if="accountStore.user.pk == store.review.user.id" @click="router.push({ name:'ReviewUpdate', params:{pk:store.review.id} })">update</button>
        <button class="delete-button" v-if="accountStore.user.pk == store.review.user.id" @click="store.deleteReview(store.review.id)">게시글 삭제</button>

      </div>
      <hr>

      <div class="comment-container list-group">
        <ReviewCommentCreate
            class="list-group-item create"
            :reviewId="store.review.id"
        />
        <ReviewCommentList
            class="list-group-item comment-list"
            v-for="comment in store.review.reviewcomment_set"
        :key="comment.id"
        :comment="comment"
        />
      </div>

    </div>
</template>

<script setup>
import { useReviewStore } from '@/stores/reviews'
import { useAccountStore } from '@/stores/accounts';
import { onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router';
import ReviewCommentCreate from '@/components/ReviewCommentCreate.vue'
import ReviewCommentList from '@/components/ReviewCommentList.vue'
import { computed } from '@vue/reactivity';
const store = useReviewStore()
const accountStore = useAccountStore()
const route = useRoute()
const router = useRouter()


const formattedDate = computed(() => {
  let date = new Date(store.review.created_at)
  let year = date.getFullYear()
  let month = ('0' + (date.getMonth() + 1)).slice(-2)
  let day = ('0' + date.getDate()).slice(-2)
  let hours = ('0' + date.getHours()).slice(-2)
  let minutes = ('0' + date.getMinutes()).slice(-2)
  return `${year}-${month}-${day} ${hours}:${minutes}`
})

const goProfile = function () {
  router.push({name:'ProfileView', params:{id:store.review.user.id}})
}


onMounted(()=>{
    store.getReviewDetail(route.params.id)
})
onMounted(()=>{
  accountStore.getuser(accountStore.token)
  window.scrollTo(0, 0);

})

</script>

<style scoped>
.menu a {
  color: rgba(255, 255, 255, 0.8);
  position: relative;
  display: block;
  text-decoration: none;
  text-transform: uppercase;
}
.SMN_effect-5 a {
  margin: 0 0px;
  padding: 18px 20px;
}

.SMN_effect-5 a:before, .SMN_effect-5 a:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 1px;
  background: #fff;
  content: '';
  opacity: 0.2;
  -webkit-transition: opacity 0.3s, height 0.3s;
  -moz-transition: opacity 0.3s, height 0.3s;
  transition: opacity 0.3s, height 0.3s;
}

.SMN_effect-5 a:after {
  top: 100%;
  opacity: 0;
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  -moz-transition: -moz-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transform: translateY(-10px);
  -moz-transform: translateY(-10px);
  transform: translateY(-10px);
}

.SMN_effect-5 a span:first-child {
  z-index: 2;
  display: block;
  font-weight: 300;
}

.SMN_effect-5 a span:last-child {
  z-index: 1;
  display: block;
  padding: 8px 0 0 0;
  color: rgba(255, 255, 255, 0.4);
  text-shadow: none;
  text-transform: none;
  font-style: italic;
  font-size: 1.5em;
  opacity: 0;
  -webkit-transition: -webkit-transform 0.3s, opacity 0.3s;
  -moz-transition: -moz-transform 0.3s, opacity 0.3s;
  transition: transform 0.3s, opacity 0.3s;
  -webkit-transform: translateY(-100%);
  -moz-transform: translateY(-100%);
  transform: translateY(-100%);
}

.SMN_effect-5 a:hover:before, .SMN_effect-5 a:focus:before {
  height: 6px;
}

.SMN_effect-5 a:hover:before, .SMN_effect-5 a:hover:after, .SMN_effect-5 a:focus:before, .SMN_effect-5 a:focus:after {
  opacity: 1;
  -webkit-transform: translateY(0px);
  -moz-transform: translateY(0px);
  transform: translateY(0px);
}

.goDetail:hover {
  color: white !important;
}

.SMN_effect-5 a:hover span:last-child, .SMN_effect-5 a:focus span:last-child {
  opacity: 1;
  -webkit-transform: translateY(0%);
  -moz-transform: translateY(0%);
  transform: translateY(0%);
}


.review-container {
  border-radius: 10px;
  background-color: rgba(92, 18, 210, 0.328);
  margin: 3% 10%;
  padding: 5%;
}
.userInfo {
  display: flex;
  flex-direction: column;
  align-items: end;
}
.userInfo p {
  margin-top: 0;
  margin-bottom: 1px;
}.comment-container {
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
    background-color: rgba(177, 177, 177, 0.532);
    border: 0;
    border-bottom: 0.5px solid black;
}
.bi:hover {
  scale: 1.2;
  color: gold;
}

.delete-button, .update-button {
  border: 0;
  border-radius: 8px;
  padding: 3px 7px;
  margin-top: 5px;
}

.delete-button:hover {
  background-color: rgba(255, 39, 1, 0.527);
  color: white;
}

.update-button:hover {
  background-color: rgba(46, 160, 12, 0.377);
  color: white;
}

</style>