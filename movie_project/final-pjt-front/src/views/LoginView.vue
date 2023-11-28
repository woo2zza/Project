<template>
    <div class="container12">
      <div class="login-container">
        <h3>로그인</h3>
        <form @submit.prevent="logIn">
          <div class="input-group mb-3">
            <label class="input-group-text" for="username">아이디</label>
            <input type="text" class="form-control" name="username" id="username" v-model="username">
          </div>
          <div class="input-group mb-3">
            <label class="input-group-text" for="password">비밀번호</label>
            <input type="password" class="form-control" name="password" v-model="password">
          </div>
          <input type="submit" class="btn">
        </form>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useAccountStore } from '@/stores/accounts'
  import { useRouter } from 'vue-router'
  
  const store = useAccountStore()
  const username = ref(null)
  const password = ref(null)
  const router = useRouter()
  
  const logIn = function (){
    const payload = {
      username: username.value,
      password: password.value,
    }
    store.logIn(payload)
    router.push({name:'MainView'})
  }
  </script>
  
  <style scoped>
.container12 {
  height: 100vh;
  width: 100%;
  margin:  0%;
  display: flex;
  flex-direction: column;
  background: black url(src/assets/judy-hopps-driving.gif) repeat-y center top;
  background-size: cover;
  overflow-y: auto;
  animation: animateBackground 20s linear infinite alternate-reverse;
  
}


.login-container {
    margin: 10% auto;
    padding: 3%;
    background:rgba(0, 0, 0, 0.8) ;
    border-radius: 10px;
    background-size: cover;
    width: 50%;
  }
  
  .input-group {
    width: 100%;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
  }
  
  .input-group-text {
    font-weight: bold;
    padding: 10px;
    width: 30%;
    background-color: rgba(0, 0, 0, 0.8);
    color: white;
    border: none;
  }
  .form-control {
  padding: 10px;
  border: none;
  background-color: rgba(255, 255, 255, 0.8);
}
  .btn {
    color: white;
    width: 100%;
    padding: 10px;
    background-color: rgb(92, 18, 210);
    border: none;
    cursor: pointer;
  }
  
  .btn:hover {
    background-color:  rgb(56, 8, 124);
  }
  
  .form-control {
    padding: 10px;
    border: none;
    background-color: rgba(255, 255, 255, 0.8);
  }
  </style>
  