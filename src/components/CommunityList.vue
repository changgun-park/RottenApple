<template>
  <v-container>
    <v-card>
      <v-card-title>
        자유게시판
        <v-spacer></v-spacer>
        
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        
        <v-btn
          class="mx-2"
          tile
          
          color="primary"
          
          @click="moveCreate"
        >
        <v-icon left>
          mdi-pencil
        </v-icon>
        CREATE
        </v-btn>
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="articles"
        :search="search"
        @click:row="rowClick"
      ></v-data-table>
      
    </v-card>
  </v-container>




  <!-- <div>
   
    <community-list-item
      v-for="article in articles"
      :key="article.id"
      :article="article"
    >
    </community-list-item>
    <br>
    <button @click="moveCreate">게시글 생성하기</button>

  </div> -->
</template>

<script>
import axios from 'axios'
// import CommunityListItem from './CommunityListItem.vue'

export default {
  // components: { CommunityListItem },
  name:'CommunityList',
  data:function(){
    return {
      search: '',
      headers: [
        
        { text: '제목', value: 'title'},
        { text: '작성자', value: 'user' },
        { text: '작성일', value: 'created_at' },
        { text: '좋아요', value: 'like_users.length' },
        
      ],
      reviews: [],

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
    rowClick: function (value) {
        // this.$router.push({name:'ReviewDetail',params:{reviewId:value.id}})
        this.$router.push({name:'Article',params:{articleNum:value.id}})
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
        console.log(res.data)
      })
      .catch(err =>{
        console.log(err)
      })
  }
}
</script>

<style>

</style>
