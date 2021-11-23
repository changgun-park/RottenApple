<template>
  <div>
    <h1>게시판 수정하기</h1>
    <v-form v-on:submit.prevent="">
      <v-text-field
        label="제목"
        outlined
        v-model="title"
      ></v-text-field>
      <v-text-field
        label="내용"
        outlined
        v-model="content"
      ></v-text-field>
      <button @click="updateArticle">수정완료</button>
    </v-form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'ArticleUpdate',
  data:function(){
    return{
      title:null,
      content:null,
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
    updateArticle:function(){
      const updateItem = {
        title:this.title,
        content:this.content
      }
     
      if (updateItem.title){
        axios({
          method:'put',
          url:`http://127.0.0.1:8000/articles/${this.$route.params.articleNum}/`,
          data:updateItem,
          headers:this.setToken(),
        })
          .then(res=>{
            console.log(res)
            this.$router.push({name:'Article',params:{articleNum:this.$route.params.articleNum}})
          })
          .catch(err=>{
            console.log(err)
          })
      }
    }
  },
  created:function(){
    this.title = this.$route.params.title
    this.content = this.$route.params.content
  }

}
</script>

<style>

</style>