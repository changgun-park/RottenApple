import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    isLogin: false,
    loginUser: null,
  },
  mutations: {
    LOGIN: function(state, username) {
      state.isLogin = true
      state.loginUser = username
    },
    LOGOUT: function(state) {
      state.isLogin = false,
      state.loginUser = false
    }
  },
  actions: {
    login: function(context, username) {
      context.commit('LOGIN', username)
    },
    logout: function(context) {
      context.commit('LOGOUT')
    }
  },
  modules: {
  }
})
