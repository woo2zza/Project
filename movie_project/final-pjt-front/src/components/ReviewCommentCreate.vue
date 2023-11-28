<template>

    <div class="comment">
        <form class="input-group mb-3 comment-form" @submit.prevent="createComment">
            <input type="text" class="form-control" placeholder="Create Comments .." name="content" id="content" v-model="content" aria-label="Recipient's username" aria-describedby="button-addon2">
            <button class="btn btn-outline-secondary" type="submit" id="button-addon2">+</button>
        </form>
    </div>
</template>

<script setup>
import { useReviewCommentStore } from '@/stores/reviewcomments'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const props = defineProps({
    reviewId:Number
})

const router = useRouter()
const store = useReviewCommentStore()
const content = ref('')
const createComment = function(){
    store.commentCreate(props.reviewId, content.value)
    router.push({name:'ReviewDetailView', params:{id:props.reviewId}})
    content.value=''
}

</script>

<style scoped>
.comment {
    width: 100%;
    height: 100%;
}
.comment-form button{
    border-bottom-right-radius: 0;

}
.comment-form input {
    background-color: rgba(138, 138, 138, 0.904);
    border: 0;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 0;
    /* width: 100%; */
    padding: 10px;

}
.comment-form input:hover {
    background-color: rgba(195, 195, 195, 0.721);
}

.comment-form input::placeholder {
  color: #c6c6c6;
}


</style>