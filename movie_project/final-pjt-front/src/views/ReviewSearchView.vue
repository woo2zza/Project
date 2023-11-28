<template>
  <div class="community-page">
    <h1 class="page-title animate__animated animate__bounce">{{ searchQuery }}의 검색 결과</h1>
    <hr>
    <div class="card-page" v-for="(video, index) in videos" :key="index">
      <YoutubeCard
        :thumbnail="video.snippet.thumbnails.default.url"
        :title="video.snippet.title"
        :descriptions="video.snippet.description"
        @click="openModal(index)"
        data-bs-toggle="modal"
        data-bs-target="#youtubeTrailerModal"
      />
    </div>

    <YoutubeReviewModal
      :videoTitle="videoTitle"
      :currentVideoId="currentVideoId"
    />
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import YoutubeReviewModal from "@/components/YoutubeReviewModal.vue";
import YoutubeCard from "@/components/YoutubeCard.vue";

const route = useRoute();
const router = useRouter();
const searchQuery = ref(route.query.q || "");
const videos = ref([]);
const currentVideoId = ref("");
const youtubeKey = import.meta.env.VITE_YOUTUBE_API_KEY;
const videoTitle = ref("");


watch(() => route.query.q, async (newQuery, oldQuery) => {
  searchQuery.value = newQuery;
  await searchReviews();
});


const searchReviews = async () => {
  try {
    const response = await axios.get("https://www.googleapis.com/youtube/v3/search", {
      params: {
        part: "snippet",
        q: searchQuery.value,
        key: youtubeKey,
        type: "video",
        maxResults: 10,
      },
    });
    videos.value = response.data.items;
  } catch (error) {
    console.error("API 호출 중 에러 발생:", error);
  }
};

const openModal = (index) => {
  const VideoId = videos.value[index].id.videoId;
  currentVideoId.value = VideoId;
  videoTitle.value = videos.value[index].snippet.title;
};


onMounted(() => {
  searchReviews();
  window.scrollTo(0, 0);
});

</script>

<style scoped>
.community-page {
    max-width: 1300px;
    margin: 0 15%;
    padding: 30px;
  }

.page-title {
  font-size: 3em;
  margin-bottom: 20px;
  text-align: center;
  color: rgb(104, 104, 104);
}

hr {
  margin-bottom: 50px;
}
</style>
