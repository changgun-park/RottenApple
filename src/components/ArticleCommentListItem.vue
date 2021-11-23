<template>
  <div>
  
      <p>{{ comment.user.username }}님의 댓글</p>
      <p>{{ comment.content }}</p>

      
      <button @click="deleteComment">댓글 삭제하기</button>


      <button v-if="!this.edit" @click="editComment">댓글 수정하기</button>
      <v-form v-else v-on:submit.prevent="">
        <v-text-field
          label="제목"
          outlined
          v-model="content"
        ></v-text-field>
        <button @click="updateComment">댓글 생성하기</button>
      </v-form>
     

    
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name:'ArticleCommentListItem',
  props:{
    comment:{
      type:Object
    },
    
  },
  data:function(){
    return {
      edit:false,
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

    deleteComment:function(){
      axios({
        method:'delete',
        url:`http://127.0.0.1:8000/article/comment/${this.comment.id}/`,
        headers:this.setToken(),
      })
        .then(res=>{
          console.log(res)
          this.$emit('delete-comment')
        })
        .catch(err=>{
          console.log(err)
        })
    },
    editComment:function(){
      this.edit = true
    },
    updateComment:function(){
      const updateItem = {
        content:this.content
      }
      axios({
        method:'put',
        url:`http://127.0.0.1:8000/article/comment/${this.comment.id}/`,
        data:updateItem,
        headers:this.setToken(),
      })
        .then(res=>{
          console.log(res)
          this.$emit('update-comment')
          this.edit = false
        })
        .catch(err=>{
          console.log(err)
        })

    }
  }

}
</script>

<style>

</style>