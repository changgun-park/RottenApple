<template>
  <div >
    <button @click="detail">{{ article.title }}</button>
  </div>
</template>

<script>
export default {
  name:'CommunityListItem',
  props:{
    article:{
      type:Object,
    }
  },
  methods:{
    detail:function(){
      this.$router.push({name:'Article',params:{articleNum:this.article.id}})
    }
  }
}
</script>

<style>

</style>