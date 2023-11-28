<template>
    <div class="comment">
        <form class="input-group mb-3 comment-form" @submit.prevent="createComment">
            <input type="text" class="form-control" placeholder="Create Comments .." aria-label="Recipient's username" aria-describedby="button-addon2" v-model="content">
            <button class="btn btn-outline-secondary" type="submit" id="button-addon2">+</button>
        </form>
    </div>
</template>

<script setup>
import { useCommentStore } from '@/stores/comments'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
const props = defineProps({
    movieId:Number
})

const router = useRouter()
const store = useCommentStore()
const content = ref('')
const createComment = function(){
    store.commentCreate(props.movieId, content.value)
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
    padding: 10px;

}
.comment-form input:hover {
    background-color: rgba(195, 195, 195, 0.721);
}

.comment-form input::placeholder {
  color: #c6c6c6;
}

</style>