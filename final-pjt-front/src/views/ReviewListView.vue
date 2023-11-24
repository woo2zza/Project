<template>
    <div class="community-page">
      <h1 class="page-title animate__animated animate__bounce">Community</h1>
      <hr>
      <div>
        <div class="search-container">
          <button @click="create" class="create-button" v-show="accountStore.isLogin">새 게시물 작성하기</button>
            <input class="search-input" v-model="title" placeholder="영화 제목을 검색해보세요!" />
            <i class="fa-solid fa-magnifying-glass" v-show="accountStore.isLogin"></i>
        </div>
      </div>
      <hr>
      <div class="review-list">
        <ReviewListItem
          v-for="review in filteredReviews"
          :key="review.id"
          :review="review"
        />
      </div>
    </div>
  </template>
  
  <script setup>
  import { useRouter } from 'vue-router'
  import { useReviewStore } from '@/stores/reviews'
  import { onMounted, ref, computed } from 'vue';
  import { useAccountStore } from '../stores/accounts';
  import ReviewListItem from '@/components/ReviewListItem.vue';
  
  const accountStore = useAccountStore()

  const router = useRouter()
  const create = function () {
    router.push({ name: 'ReviewCreate' })
  }
  
  const store = useReviewStore()

  const title = ref('')

  const filteredReviews = computed(() => {
    const searchTerm = title.value.toLowerCase().trim();
    if (!searchTerm) {
      return store.reviews
    } else {
      return store.reviews.filter(review =>
        review.movie.title.toLowerCase().trim().includes(searchTerm)
      );
    }
  });

  
  onMounted(() => {
    store.getReviewList()
    window.scrollTo(0, 0);

  })
  </script>
  
  <style scoped>
  .community-page {
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
  
  .create-button {
    background-color: rgb(51, 9, 99); 
    height: 50px;
    width: 17%;
    font-size: 1em;
    cursor: pointer;
    border: none;
    border-radius: 5px;
    margin-bottom: 20px;
    color: rgb(192, 192, 192);
  }
  
  .create-button:hover {
    background-color: rgb(57, 10, 110);
    color: white;
  }
  
  .review-list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
  }
  
 
  .search-container {
    display: flex;
    justify-content: space-between;
}

  .search-input {
      background-color: rgba(255, 255, 255, 0.26);
      border: 0;
      border-radius: 20px;
      padding: 0.3rem 0.7rem;
      width: 40%;
      height: 33px;

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
  .search-input {
    padding-right: 30px;
  }

  .fa-magnifying-glass {
    position: absolute;
    top: 23%;
    right: 10px;
    transform: translateY(-50%);
  }
 
  </style>
  