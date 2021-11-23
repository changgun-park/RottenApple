<template>
  <div>
   
    <community-list-item
      v-for="article in articles"
      :key="article.id"
      :article="article"
    >
    </community-list-item>
    <br>
    <button @click="moveCreate">게시글 생성하기</button>

  </div>
</template>

<script>
import axios from 'axios'
import CommunityListItem from './CommunityListItem.vue'

export default {
  components: { CommunityListItem },
  name:'CommunityList',
  data:function(){
    return {
      articles:[],
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

    moveCreate:function(){
      this.$router.push({ name: 'ArticleCreate' })
    }
  },
  created:function(){
    
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/articles/',
      // headers: this.setToken()
      
    })
      .then(res =>{
        this.articles = res.data
      })
      .catch(err =>{
        console.log(err)
      })
  }
}
</script>

<style>

</style>
