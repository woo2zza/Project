<template>
    <div class="follower-container">
        <span class="username">{{ follower.username }}</span>
        <span @click="goprofile">
            <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" class="bi bi-house-fill mb-1" viewBox="0 0 16 16">
            <path d="M8.707 1.5a1 1 0 0 0-1.414 0L.646 8.146a.5.5 0 0 0 .708.708L8 2.207l6.646 6.647a.5.5 0 0 0 .708-.708L13 5.793V2.5a.5.5 0 0 0-.5-.5h-1a.5.5 0 0 0-.5.5v1.293L8.707 1.5Z"/>
            <path d="m8 3.293 6 6V13.5a1.5 1.5 0 0 1-1.5 1.5h-9A1.5 1.5 0 0 1 2 13.5V9.293l6-6Z"/>
            </svg>
        </span>
    </div>
</template>

<script setup>
import { computed } from '@vue/reactivity';
import { useRouter } from 'vue-router';
import { RouterLink } from 'vue-router';
import { useAccountStore } from '@/stores/accounts';
const store = useAccountStore()
const router = useRouter()
const props = defineProps({
    follower:Object
})

const goprofile = () =>{
    store.getprofile(props.follower.id)
    router.push({name:'ProfileView', params:{id:props.follower.id}})
}



</script>

<style scoped>
.follower-container {
    display: flex;
    justify-content: space-between;
    background-color: rgba(94, 94, 94, 0.507);
    border: 0;
}
.username {
    color: white;
}
.username:hover {
    font-weight: 700;
    color: rgb(64, 0, 125);
}

.bi:hover {
    scale: 1.2;
    color: gold;
}

</style>