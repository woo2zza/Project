<template>
  <div class="main-container">
    <HeaderNavbar />
    <RouterView />
  </div>
  <div class="foot">
    <FooterView />
  </div>

</template>

<script setup>
import HeaderNavbar from './components/common/HeaderNavbar.vue';
import FooterView from '@/components/common/FooterView.vue';
import { RouterView } from 'vue-router';
import { onMounted } from 'vue';
import { useAccountStore } from './stores/accounts';
const accountStore = useAccountStore()


onMounted(()=>{
  accountStore.isLogin
})

</script>

<style scoped>
.main-container {
  min-height: 100vh;
  background-image: linear-gradient(to bottom, #000000, #121212, #1d1d1d, #282828, #343434, #363636, #393939, #3b3b3b, #353535, #2f2f2f, #292929, #232323);
  min-height: 100vh;
  width: 100%;
}

.foot {
  min-height: 15vh;
  background-color: black;
  width: 100%;
}

* {
  color: white;
}

</style>