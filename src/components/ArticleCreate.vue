<template>
  <div>
    <h1>게시판 등록</h1>
    <form action="">
      <table>
        <colgroup></colgroup>
      </table>
    </form>
  </div>
</template>

<script>
export default {
  name:'ArticleCreate',
  data:function(){
    return{
      title:null,
      content:null,
    }
  },
  methods:{
    createArticle:function(){
      const createItem = {
        title:this.title,
        content:this.content
      }
      if (createItem.title){
        axios({
          method:'post',
          url:''
        })
      }
    }
  }

}
</script>

<style>

</style>