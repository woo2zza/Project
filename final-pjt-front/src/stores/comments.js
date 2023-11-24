import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useMovieStore } from './movies.js'
import { useAccountStore } from './accounts.js'


export const useCommentStore = defineStore('comments', () => {
    const movieStore = useMovieStore()
    const accountStore = useAccountStore()
    const commentCreate = function(id, content) {
        axios({
            method:'post',
            url:`http://127.0.0.1:8000/movies/${id}/comments/`,
            data:{
                content
            },
            headers: {
                Authorization: `Token ${accountStore.token}`
            }
        })
        .then((res)=>{
            movieStore.movie.moviecomment_set.push(res.data)
        })
        .catch((err)=>console.log(err))
    }


    const commentDelete = function(commentPk) {
        axios({
            method: 'delete',
            url: `http://127.0.0.1:8000/movies/comments/${commentPk}/`,
            headers: {
                Authorization: `Token ${accountStore.token}`
            }
        })
        .then((res) => {
            movieStore.movie.moviecomment_set = movieStore.movie.moviecomment_set.filter((comment) => {
                return comment.id != commentPk
            })
        })
        .catch(err => {
            console.log(err)
        })
    }

    return{ commentCreate, commentDelete }
}, { persist: true })
