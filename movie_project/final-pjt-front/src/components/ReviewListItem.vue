<template>
    <div class="reviewList" style="18rem">
        <div class="reviewlistitem">
            <div class="text">
                <h4>{{ review.movie.title }}</h4>
                <hr>
                <h5>{{ review.title }}</h5>
                <div class="review-content">
                    {{ review.content }}
                </div>
                <hr>
                <div class="bottom-container">
                    <p>{{ review.user.username }}</p>
                    <button @click="goReviewDetail">자세히</button>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { RouterLink } from 'vue-router'

const props = defineProps({
    review:Object
})

const router = useRouter()
const goReviewDetail = function () {
  router.push({name:'ReviewDetailView', params:{id:props.review.id}})
}

</script>

<style scoped>


.reviewlistitem {
    height: 270px;
    background-color: rgba(51, 51, 51, 0.792);
    padding: 3%;
    margin : 10px;
    border : 1px solid rgb(230, 224, 224);
    border-radius: 18px;
    box-shadow: 0 2px 2px rgb(112, 111, 111);
}

.reviewlistitem:hover {
    background-color: rgba(68, 68, 68, 0.792);

}

.text {
    margin : 3% 25px;
}

.review-content {
    max-width: calc(100% - 38px);
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
}

.bottom-container {
    display: flex;
    justify-content: space-between;
}

button {
    border: 0;
    border-radius: 10px;
    padding: 0 12px;
    background-color: rgb(51, 9, 99);
    color: rgb(192, 192, 192);
}
button:hover {
    background-color: rgb(57, 10, 110);
    color: white;
}

</style>