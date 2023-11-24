<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary sticky-top">
    <div class="container-fluid">
      <RouterLink class="navbar-brand mainlogo animate__animated animate__rubberBand" :to="{ name: 'MainView' }">
        MovieSignal <img src="@/assets/moviesignal-unscreen.gif" style="width: 60px;" alt="">
      </RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse justify-content-between" id="navbarNav">
        <ul class="navbar-nav left-items">
          <li class="nav-item">
            <RouterLink :to="{ name: 'MovieListView' }" class="nav-link" active-class="active-tab">movie-list</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'ReviewListView' }" class="nav-link" active-class="active-tab">review</RouterLink>
          </li>
        </ul>



        <ul class="navbar-nav right-items">
          <li class="input_box nav-link p-0" style="justify-content: flex-end;">
            <div class="input-group me-3">
              <input
                placeholder="콘텐츠, 인물, 컬렉션, 유저를 검색해보세요."
                type="text"
                class="form-control"
                v-model="searchQuery"
                v-on:keyup.enter="goToSearch"
                />
              <button @click="goToSearch" class="search-button btn btn-outline-secondary">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
                </svg>
              </button>
            </div>
          </li>

        <ul class="menu navbar-nav right-items me-0 pe-0">
          <li>
            <a v-show="!isLogin" @click="router.push({name:'SignUpView'})">Signup</a>
          </li>
        </ul>
        <ul class="menu navbar-nav right-items">
          <li>
            <a v-show="!isLogin" @click="router.push({name:'LoginView'})">Login</a>
            <a v-if="accountStore.userpk">{{ accountStore.user.username }}</a>
            <div class="child-link" v-if="accountStore.userpk">
              <p class="nav-link" @click="router.push({ name : 'ProfileView', params:{id:accountStore.userpk}})" active-class="active-tab">profile</p>
              <p class="nav-link" @click="accountStore.logout" active-class="active-tab">logout</p>
            </div>
          </li>
        </ul>
      </ul>


      </div>
    </div>
  </nav>

</template>

<script setup>
import 'animate.css';
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router';
import { useAccountStore } from '@/stores/accounts'
import { onMounted, computed } from 'vue';
const searchQuery = ref("");
const accountStore = useAccountStore()
const router = useRouter()
const goToSearch = function() {
  router.push({ name: 'ReviewSearchView', query: { q: `영화 ${searchQuery.value}` } });
}

const isLogin = computed(() => {
  accountStore.getuser(accountStore.token)
  return accountStore.isLogin ? true : false
})



onMounted(()=>{
  accountStore.getuser(accountStore.token)
  accountStore.isLogin
  // router.push({name:'MainView'})
})

</script>

<style scoped>
.menu {
  display: block;
  position: relative;
  /* width: 200px; */
}

.menu > li > a {
  background: rgb(51, 9, 99);
  border-radius: 30px;
  color: #fff;
  display: block;
  padding: 10px 23px;
  text-align: center;
  text-decoration: none;
}

.menu div {
  background: rgba(0, 0, 0, 0.577);
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  height: 0;
  left: 0;
  opacity: 0;
  padding-bottom: 7px;
  position: absolute;
  transition: all .5s ease;
  width: 100%;
}

.menu li:hover div {
  height: auto;
  opacity: 1;
  transform: translateY(0);
}

.menu div p {
  text-align: center;
  color: rgb(84, 84, 84);
  display: block;
  margin: 4px 0;
  font-weight: 100;
  font-size: 18px;

}


.input_box {
  display: flex;
  align-items: center;
  height: 100%;
  /* margin: 0px 0px 0px auto; */
  margin-top: 5px;
  color: white;
}


.location {
  display: flex;
  /* position: relative; */
  width: 300px;
}
.form-control {
  font-size: 15px;
  background-color: rgba(0, 0, 0, 0.1);
  border: 1px solid rgb(97, 97, 97);
}
.form-control:hover {
  border-color: white;
}

.input-group {
  width: 370px;
}

.form-control::placeholder {
  color: #878787;
}
.form-control {
  color: white;
}

.search-button {
  font-size: 0.5rem;
  background-color: #c6c7c9;
  border: none;
  cursor: pointer;
}

.navbar-brand {
  color: white;
  font-size: 25px
}
.navbar {
  background: linear-gradient(rgb(0, 0, 0), rgb(0, 0, 0));
  color: white;
  height: 55px;
}

.container-fluid {
  background-color: rgba(9, 9, 9, 0.665);
}


.nav-link {
  color: white;
  font-size: 20px;
  font-weight: 200;
}
.nav-link:hover {
  font-size:21px
}

.menu div p:hover {
  font-size: 18px;
  color: rgb(255, 255, 255);
}

@media (max-width: 992px) {
  .right-items {
    display: none !important;
  }
}

.active-tab {
  color: rgb(93, 15, 229) !important;
}

</style>
