<template>
  <div class="container23">
    <div class="signup-container">
      <h3>회원가입</h3>
      <form @submit.prevent="signUp">
        <div class="input-group mb-3">
          <label class="input-group-label" for="username">아이디</label>
          <input
            type="text"
            class="form-control"
            name="username"
            id="username"
            v-model="username"
          />
        </div>

        <div class="input-group mb-3">
          <label class="input-group-label" for="password1">비밀번호</label>
          <input
            type="password"
            class="form-control"
            name="password1"
            v-model="password1"
          />
        </div>

        <div class="input-group mb-3">
          <label class="input-group-label" for="password2"
            >비밀번호 재확인</label
          >
          <input
            type="password"
            class="form-control"
            name="password2"
            v-model="password2"
          />
        </div>

        <input type="submit" class="btn" value="회원가입" />
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAccountStore } from "@/stores/accounts";
import { useRouter } from "vue-router";

const router = useRouter();
const store = useAccountStore();

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
  };
  store.signUp(payload);
};
</script>

<style scoped>
.container23 {
  height: 100vh;
  width: 100%;
  margin:  0%;
  display: flex;
  flex-direction: column;
  background: url(src/assets/17.gif) repeat-y center top;
  background-size: cover;
  overflow-y: auto;
  animation: animateBackground 20s linear infinite alternate-reverse;
}

.signup-container {
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

.input-group-label {
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
  width: 100%;
  padding: 10px;
  border: none;
  background-color: rgb(92, 18, 210);
  color: white;
  cursor: pointer;
}

.btn:hover {
  background-color: rgb(56, 8, 124);
}

.form-control {
    padding: 10px;
    border: none;
    background-color: rgba(255, 255, 255, 0.8);
  }
</style>
