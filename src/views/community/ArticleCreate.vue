<template>
  <div>
    <h1>게시판 등록</h1>
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
      <button @click="createArticle">생성하기</button>
    </v-form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'ArticleCreate',
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
    createArticle:function(){
      const createItem = {
        title:this.title,
        content:this.content
      }
     
      if (createItem.title){
        axios({
          method:'post',
          url:'http://127.0.0.1:8000/articles/',
          data:createItem,
          headers:this.setToken(),
        })
          .then(res=>{
            console.log(res)
            this.$router.push({ name: 'Community' })
          })
          .catch(err=>{
            console.log(err)
          })
      }
    }
  }

}
</script>

<style>

</style>