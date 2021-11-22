<template>
  <div>
    <p>{{article.id}}</p>
    <p>{{article.title}}</p>
    <p>{{article.content}}</p>
    <p>{{ article.like_users.length }}</p>
    <button @click="getlike">like</button>
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'ArticleDetail',
  data:function(){
    return{
      article:[]
    }
  },
  methods:{
    getlike:function(){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/articles/${this.article.id}/likes/`
      })
        .then(res=>{
        console.log(res)
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
  created:function(){
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/articles/${this.$route.params.articleNum}`,

    })
      .then(res=>{
        console.log(res)
        this.article = res.data
      })
      .catch(err=>{
        console.log(err)
      })
  }
}
</script>

<style>

</style>