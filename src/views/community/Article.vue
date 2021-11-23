<template>
  <div>
    <h1>{{ $route.params.articleNum }}</h1>
    <article-detail></article-detail>
    <article-comment-list
    :articleNum="$route.params.articleNum"
    ></article-comment-list>

    
    
  </div>
</template>

<script>
import ArticleDetail from '@/components/ArticleDetail'
import ArticleCommentList from '@/components/ArticleCommentList'


export default {
  name:'Article',
  components:{
    ArticleDetail,
    ArticleCommentList,
    
  },
}
</script>

<style>
    

</style>