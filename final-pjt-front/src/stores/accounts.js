import axios from 'axios'
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

export const useAccountStore = defineStore('accounts', () => {
    
    const token = ref(null)
    const user = ref(null)
    const userpk = ref(null)
    const router = useRouter()

    
    const signUp = function (payload){
        const { username, password1, password2 } = payload
        axios({
            method:'post',
            url: 'http://127.0.0.1:8000/accounts/signup/',
            data:{
                username, password1, password2
            }
        })
        .then((res)=>{
            const password = password1
            logIn({ username, password })
        })
        .catch((err)=>console.log(err))
    }

    const logIn = function (payload){
        const { username, password } = payload
        axios({
            method:'post',
            url: 'http://127.0.0.1:8000/accounts/login/',
            data: {
                username, password
            }
        })
        .then((res)=>{
            token.value = res.data.key
            router.push({name:'MainView'})
        })
        .catch((err)=>console.log(err))
    }

    const isLogin = computed(()=>{
        if (token.value === null){
            return false
        } else{
            return true
        }
    })

    const logout = () => {
        token.value = null;
        isLogin.value = false;
        user.value = null;
        userpk.value = null;
        router.push({ name: "MainView" });
      };

    
    const getuser = function (token) {
    axios({
        method:'get',
        url: 'http://127.0.0.1:8000/accounts/user/',
        headers: {
            Authorization: `Token ${token}`
            }
        })
        .then((res)=>{
            userpk.value = res.data.pk
            user.value = res.data
        })
    }

    const profiles = ref([])

    const getprofile = function(id) {
      axios({
        method:'get',
        url: `http://127.0.0.1:8000/profile/${id}/`
      })
      .then((res)=>{
        profiles.value = res.data
      })
      .catch((err)=>console.log(err))
    }
    

    const follow = function (id, usertoken) {
        axios({
            method:'post',
            url: `http://127.0.0.1:8000/profile/${id}/follow/`,
            headers: {
                Authorization: `Token ${usertoken}`
                }
        })
        .then((res)=>{
            getprofile(id)
        })
        .catch((err)=>console.log(err))
    }


    return { signUp, logIn, token, isLogin, logout, getuser, user, userpk, getprofile, profiles, follow, userpk }
}, { persist: true })
