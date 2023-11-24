import axios from 'axios'
import { defineStore } from 'pinia'
import { useReviewStore } from './reviews.js'
import { useAccountStore } from './accounts.js'
import { useRouter } from 'vue-router'


export const useReviewCommentStore = defineStore('reviewcomments', () => {
    const reviewStore = useReviewStore()
    const accountStore = useAccountStore()
    const commentCreate = function(id, content) {
        axios({
            method:'post',
            url:`http://127.0.0.1:8000/movies/reviews/${id}/comments/`,
            data:{
                content
            },
            headers: {
                Authorization: `Token ${accountStore.token}`
            }
        })
        .then((res)=>{
            reviewStore.review.reviewcomment_set.push(res.data)
        })
        .catch((err)=>console.log(err))
    }

    const router = useRouter()
    const commentDelete = function(commentPk) {
        axios({
            method:'delete',
            url:`http://127.0.0.1:8000/movies/reviews/comments/${commentPk}/`,
            headers: {
                Authorization: `Token ${accountStore.token}`
            }
        })
        .then((res)=>{
            reviewStore.review.reviewcomment_set = reviewStore.review.reviewcomment_set.filter((reviewcomment) => {
                return reviewcomment.id != commentPk
            })
        })
        .catch((err)=>console.log(err))
    }

    return{ commentCreate, commentDelete }
}, { persist: true })
