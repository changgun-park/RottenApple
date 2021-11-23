// import Vue from 'vue'
// import Vuex from 'vuex'
// import axios from 'axios'

// Vue.use(Vuex)

// export default new Vuex.Store({
//   state: {
//     liked:null,
//     article:null,
//     articles:[],
//   },
//   mutations: {
//     GET_ARTICLES:function(state,data){
//       state.articles=data
//     },
//     GET_ARTICLE_DETAIL:function(state,data){
//       state.article = data
//       console.log()
//     },
//     GET_LIKE:function(state){
//       console.log(state)
//     }
//   },
//   actions: {
    
//     GetArticles:function({commit}){
//       axios({
//         method:'get',
//         url:'http://127.0.0.1:8000/articles/'
        
//       })
//         .then(res =>{
//           console.log(res)
//           commit('GET_ARTICLES',res.data)
//         })
//         .catch(err =>{
//           console.log(err)
//         })


//       },
//     GetArticleDetail:function({commit},param) {
//       axios({
//         method:'get',
//         url:`http://127.0.0.1:8000/articles/${param}`,
        
//       })
//       .then(res=>{
//           console.log(res)
//           this.article = res.data
//           commit('GET_ARTICLE_DETAIL',res.data)
//         })
//         .catch(err=>{
//           console.log(err)
//         })
//       },
      
//     GetLike:function({commit}){
//       commit('GET_LIKE')
//     },
//   },
//   modules: {
//   }
// })
