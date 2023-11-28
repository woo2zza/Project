import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export const fetchMovieArticles = (Pk) => {
  return axios
    .get(`${API_URL}/movies/${Pk}/articles/`)
    .then((response) => {
      return response
    })
    .catch((error) => {
      console.error('API 요청 중 에러가 발생했습니다:', error)
      throw error
    })
}