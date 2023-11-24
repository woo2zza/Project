<template>
    <div class="comment-container">
        <div class="right">
            <span class="username" @click="goProfile">{{ comment.user.username }}</span>
             - {{ comment.content }}
        </div>
        <div class="left">
            <span>{{ formattedDate }}</span>
            <button v-show="isUser" class="delete-button" @click="commentDelete">삭제</button>
        </div>
    </div>
</template>

<script setup>
import { computed } from '@vue/reactivity';
import { useRouter } from 'vue-router';
import { useCommentStore } from '@/stores/comments';
import { useAccountStore } from '../stores/accounts';

const accountStore = useAccountStore()
const store = useCommentStore()
const router = useRouter()
const props = defineProps({
    comment:Object
})
const commentDelete = function () {
    store.commentDelete(props.comment.id)
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

const isUser = computed(()=>{
    accountStore.isLogin
    accountStore.getuser(accountStore.token)
    return accountStore.userpk === props.comment.user.id ? true : false
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
    background-color: rgb(126, 126, 126);
    padding: 4px 7px;
    border-radius: 20px;
    font-weight: 500;
}
.username:hover {
    scale: 1.2;
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