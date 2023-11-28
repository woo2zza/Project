import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import MovieListView from '@/views/MovieListView.vue'

import ReviewListView from '@/views/ReviewListView.vue'
import ReviewFormView from '@/views/ReviewFormView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ReviewSearchView from '@/views/ReviewSearchView.vue'
import LoginView from '@/views/LoginView.vue'
import ProfileView from '@/views/ProfileView.vue'

import { useAccountStore } from '@/stores/accounts'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    { 
      path:'/movies',
      name: 'MovieListView',
      component: MovieListView
    },
    { 
      path:'/movies/:id',
      name: 'MovieDetailView',
      component: MovieDetailView
    },
    {
      path:'/review',
      name: 'ReviewListView',
      component: ReviewListView
    },
    {
      path:'/review/create',
      name: 'ReviewCreate',
      component: ReviewFormView
    },
    {
      path:'/review/:id',
      name: 'ReviewDetailView',
      component: ReviewDetailView
    },
    {
      path:'/signup',
      name:'SignUpView',
      component:SignUpView
    },
    {
      path: '/review-search',
      name: 'ReviewSearchView',
      component: ReviewSearchView
    },
    {
      path:'/login',
      name:'LoginView',
      component:LoginView
    },
    {
      path:'/profile/:id',
      name:'ProfileView',
      component:ProfileView
    },
    {
      path: '/review/:pk',
      name: 'ReviewUpdate',
      component: ReviewFormView
    },

  ]
})

router.beforeEach((to, from) => {
  const store = useAccountStore()
  if ((to.name === 'SignUpView' || to.name === 'LoginView') && (store.isLogin)){
    return { name:'MainView'}
  }
})

export default router
