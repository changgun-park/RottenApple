import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    isLogin: false,
    loginUser: 'Anonymous',
    movieCards:[],
  },
  mutations: {
    LOGIN: function(state, username) {
      state.isLogin = true
      state.loginUser = username
    },
    LOGOUT: function(state) {
      state.isLogin = false,
      state.loginUser = 'Anonymous'
    },
    LOAD_MOVIE_CARDS:function(state,data){
      state.movieCards = data
    },
  },
  actions: {
    login: function(context, username) {
      context.commit('LOGIN', username)
    },
    logout: function(context) {
      context.commit('LOGOUT')
    },
    LoadMovieCards:function({commit}) {
      axios({
        method:'get',
        url:'http://127.0.0.1:8000/movies/',
      })
        .then(res=>{
          // console.log(res)
          commit('LOAD_MOVIE_CARDS',res.data)
          
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
  modules: {
  }
})
