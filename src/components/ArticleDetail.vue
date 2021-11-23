<template>
  <div>
    <p>id : {{id}}</p>
    <h1>{{title}}</h1>
    <p> content : {{content}}</p>
    <p>like count : {{ like_users }}</p>
    <button @click="getlike">like</button>
    <button @click="moveUpdate">수정하기</button>
    <button @click="deleteData(id)">삭제하기</button>
    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'ArticleDetail',
  data:function(){
    return{
      
      category:null,
      id:null,
      content:null,
      created_at:null,
      like_users:null,
      rate:null,
      title:null,
      user:null,
    }
  },
  methods:{
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    moveUpdate:function(){
      this.$router.push({name:'ArticleUpdate',params:{articleNum:this.id,title:this.title,content:this.content}})
    },
    deleteData:function(id){
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/articles/${id}/`,
        headers:this.setToken()
      })
        .then(res=>{
          console.log(res)
          this.$router.push({name:'Community'})
        })
        .catch(err=>{
          console.log(err)
        })
    },
    getlike:function(){
      axios({
        method:'post',
        url:`http://127.0.0.1:8000/articles/${this.$route.params.articleNum}/likes/`,
        headers:this.setToken()
      })
        .then(()=>{
          this.getData()
        })
        .catch(err=>{
          console.log(err)
          
        })
    },
    getData:function() {
      // console.log(this.$route.params.articleNum)
    axios({
      method:'get',
      url:`http://127.0.0.1:8000/articles/${this.$route.params.articleNum}`,

    })
      .then(res=>{
        
        this.category = res.data.category
        this.content = res.data.content
        this.title = res.data.title
        this.id = res.data.id
        this.like_users = res.data.like_users.length
        this.created_at = res.data.created_at
        this.user = res.data.user
        this.rate = res.data.rate
      })
      .catch(err=>{
        console.log(err)
      })
    }
  },
  
  created:function(){
    this.getData()
  }
}
</script>

<style>

</style>
