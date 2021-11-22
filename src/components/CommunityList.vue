<template>
  <div>
   
    <community-list-item
      v-for="article in articles"
      :key="article.id"
      :article="article"
    >
    </community-list-item>

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
  created:function(){
    axios({
      method:'get',
      url:'http://127.0.0.1:8000/articles/'
      
    })
      .then(res =>{
        console.log(res)
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