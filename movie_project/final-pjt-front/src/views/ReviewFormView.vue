<template>
<div class="review-create-page">
    <div class="review-create-container">
    <h1 v-if="route.name === 'ReviewCreate'" class="page-title">Review Create</h1>
    <h1 v-else class="page-title">Review Update</h1>
    <hr>
    <form @submit.prevent="route.name === 'ReviewCreate'? createReview() : updateReview()" class="review-form">
    <label for="movie" class="form-label">영화</label>
    <select name="movie" id="movie" v-model="movie" class="form-input">
        <option v-for="movie in store.movieTitle" :key="movie.id" :value="movie.id">
        {{ movie.title }}
        </option>
    </select>
    <br />

    <label for="title" class="form-label">제목</label>
    <input type="text" name="title" id="title" v-model="title" class="form-input" />
    <br />

    <label for="content" class="form-label">내용</label>
    <textarea
        name="content"
        id="content"
        rows="5"
        cols="50"
        v-model="content"
        class="form-input"
    ></textarea>
    <br />

    <button v-if="route.name === 'ReviewCreate'" type="submit" class="submit-button">게시글 작성</button>
    <button v-if="route.name === 'ReviewUpdate'" type="submit" class="submit-button">게시글 수정</button>
</form>
</div>
</div>
</template>

<script setup>
import { useReviewStore } from '@/stores/reviews';
import { onMounted, ref } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const route = useRoute()
const router = useRouter();

const store = useReviewStore();
onMounted(() => {
    store.getMovieTitle()
    if (route.name === 'reviewUpdate') {
        store.reviewstore(route.params.pk)
    }
    window.scrollTo(0, 0);
});

const movie = ref('');
const title = ref('');
const content = ref('');

const createReview = () => {
    const review = {
        movie: movie.value,
        title: title.value,
        content: content.value,
    };
    store.createReview(review);
    router.push({ name: 'ReviewListView' })
    store.getReviewList()
};

const updateReview = () => {
    const review = {
    pk: route.params.pk,            
    movie: movie.value,
    title: title.value,
    content: content.value,
    };
    store.updateReview(review);
    router.push({ name: 'ReviewDetailView', params:{id:review.pk}})
    store.getReviewDetail(review.pk)
};



</script>

<style lang="scss" scoped>
.review-create-page {
max-width: 60%;
margin: 3% auto;
padding: 20px;
background-color: #14141470;
border-radius: 10px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}



.page-title {
font-size: 2em;
text-align: center;
color: #fff;
margin: 20px 0;
}

.review-form {
display: flex;
flex-direction: column;
}

.form-label {
margin-bottom: 5px;
color: #fff;
}

.form-input {
padding: 8px;
margin-bottom: 10px;
border: 1px solid #ddd;
border-radius: 5px;
background-color: #fff; /* White color */
color: #333; /* Dark grey color */
}

.submit-button {
background-color: rgb(51, 9, 99);
color: #fff;
padding: 10px 15px;
border: none;
border-radius: 5px;
cursor: pointer;
}

.submit-button:hover {
background-color: rgb(39, 7, 77);
}
</style>
