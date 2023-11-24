import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useAccountStore } from './accounts.js'


export const useReviewStore = defineStore('reviews', () => {
  const reviews = ref([])
  const accountStore = useAccountStore()

  const getReviewList = function () {
    axios({
      method:'get',
      url: 'http://127.0.0.1:8000/movies/reviews/',
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then((res)=>{
        reviews.value = res.data
    })
    .catch((err)=>console.log(err))
  }

  const movieTitle = ref([])

  const getMovieTitle = function(){
    axios({
        method:'get',
        url: 'http://127.0.0.1:8000/movies/title/',
        headers: {
          Authorization: `Token ${accountStore.token}`
        }
    })
    .then((res)=>{
        movieTitle.value = res.data
    })
    .catch((err)=>console.log(err))
  }

  const createReview = function ({movie, title, content}) {
    axios({
        method:'post',
        url: 'http://127.0.0.1:8000/movies/reviews/',
        data : {
            movie,
            title,
            content,
        },
        headers: {
          Authorization: `Token ${accountStore.token}`}
    })
  }

  const review = ref([])
  const getReviewDetail = function (pk) {
    axios({
      method:'get',
      url: `http://127.0.0.1:8000/movies/reviews/${pk}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`}
    })
    .then((res)=>{
      review.value = res.data
    })
    .catch((err)=>console.log(err))
  }
  
  const router = useRouter()
  const deleteReview = function(pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/movies/reviews/${pk}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then(res => router.push({name:'ReviewListView'}))
  }

  const updateReview = function ({pk, movie, title, content}) {
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/movies/reviews/${pk}/`,
      data: {
        movie,
        title,
        content
      },
      headers: {
        Authorization: `Token ${accountStore.token}`}
    })
  }

  return { reviews, getReviewList, movieTitle, getMovieTitle, createReview, review, getReviewDetail, deleteReview, updateReview }
}, { persist: true })
