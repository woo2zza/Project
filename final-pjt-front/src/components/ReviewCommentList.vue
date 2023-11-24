<template>
    <div class="comment-container">
        <span class="left">
            <span class="username" @click="goProfile">{{ comment.user.username }}</span>
             - {{ comment.content }}</span>
        <div class="right">
            <span>{{ formattedDate }}</span>
            <button class="delete-button" @click="deleteComment">삭제</button>
        </div>
    </div>
</template>

<script setup>
import { computed } from '@vue/reactivity';
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useReviewCommentStore } from '@/stores/reviewcomments';
import { useReviewStore } from '@/stores/reviews'

const reviewStore = useReviewStore()
const store = useReviewCommentStore()
const router = useRouter()
const props = defineProps({
    comment:Object
})

const deleteComment = function () {
    store.commentDelete(props.comment.id)
    router.push({name:'ReviewDetailView', params:{id:props.comment.review.id}})
    reviewStore.getReviewDetail(props.comment.review.id)
}


const formattedDate = computed(() => {
  let date = new Date(props.comment.created_at)
  let year = date.getFullYear()
  let month = ('0' + (date.getMonth() + 1)).slice(-2)
  let day = ('0' + date.getDate()).slice(-2)
  let hours = ('0' + date.getHours()).slice(-2)
  let minutes = ('0' + date.getMinutes()).slice(-2)
  return `${year}-${month}-${day} ${hours}:${minutes}`
})

const goProfile = function () {
  router.push({name:'ProfileView', params:{id:props.comment.user.id}})
}



</script>

<style scoped>
.comment-container {
    display: flex;
    justify-content: space-between;
}
.username {
    font-weight: 500;
}
.username:hover {
    scale: 1.1;
    font-weight: 700;
    color: rgb(64, 0, 125);
}

.delete-button {
    margin-left: 10px;
    border: 0;
    background-color: rgb(102, 102, 102);
    border-radius: 4px;
}
.delete-button:hover {
    color: white;
}

</style>