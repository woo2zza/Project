import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'
import { useAccountStore } from './accounts'



export const useMovieStore = defineStore('movies', () => {
  const router = useRouter()
  const accountStore = useAccountStore()
  const movies = ref([])
  const getMovieList = function () {
    axios({
      method:'get',
      url: 'http://127.0.0.1:8000/movies/'
    })
    .then((res)=>{
      movies.value = res.data
    })
    .catch((err)=>console.log(err))
  }


  const movie = ref([])
  const getMovieDetail = function (pk) {
    axios({
      method:'get',
      url: `http://127.0.0.1:8000/movies/${pk}/`
    })
    .then((res)=>{
      movie.value = res.data
    })
    .catch((err)=>console.log(err))
  }

  const key = import.meta.env.VITE_TMDB_API_KEY

  const fetchMovieDetail = (movieId) => {
    const url = `https://api.themoviedb.org/3/movie/${movieId}?language=ko-KR`
      const headers = {
        accept: 'application/json',
        Authorization: `Bearer ${key}`
      }
    axios.get(url, { headers })
    .then((res)=>{
      movie.value = res.data
    })
    .catch((err)=>{
      console.log(err)
    })
  }

  const topmovies = ref(null)
  const TopMovie = () => {
    const URL = 'https://api.themoviedb.org/3/movie/top_rated?language=ko-KR&page=3';
    const headers = {
      accept: "application/json",
      Authorization: `Bearer ${key}`,
    };
    axios.get(URL, { headers })
    .then((response) => {
      topmovies.value = response.data.results.slice(0, 10)
    })
    .catch((error)=>{
      console.log(error)
    })
  }

  const likeMovie = (id) => {
    axios({
      method:'post',
      url:`http://127.0.0.1:8000/movies/${id}/like/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then((res)=>{
      getMovieDetail(id)
    })
    .catch((err)=>{
      console.log(err)
    })
  }


  return { movies, getMovieList, movie, getMovieDetail, TopMovie, topmovies, likeMovie, fetchMovieDetail, }
}, { persist: true })
