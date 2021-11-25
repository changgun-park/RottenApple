<template>
  <v-container>
    <v-card>
      <v-card-title>
        리뷰 목록
        <v-spacer></v-spacer>
        
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        ></v-text-field>
        <v-btn class="ml-5" :to="{ name: 'ReviewCreate' }">글쓰기</v-btn>
      </v-card-title>
      <!-- @click:row="handleClick" 각 열 클릭시 handleClick 메서드 호출 -->
      <v-data-table
        :headers="headers"
        :items="reviews"
        :search="search"
        @click:row="rowClick"
      ></v-data-table>
      
    </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'

  export default {
    name: 'ReviewIndex',
    data: function () {
      return {
        search: '',
        headers: [
          { text: '영화', value: 'movie', align: 'start'},
          { text: '제목', value: 'title'},
          { text: 'ID', value: 'user' },
          { text: '작성일', value: 'created_at' },
          { text: '조회수', value: 'views', sortable: true },
        ],
        reviews: [],
        title: null,
      }
    },
    methods: {
      setToken:function () {
        const token = localStorage.getItem('jwt')
        const config = {
          Authorization: `JWT ${token}`
        }
      return config
      },
      rowClick: function (value) {
        this.$router.push({name:'ReviewDetail',params:{reviewId:value.id}})
      }
    },
    created: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/reviews/list/',
        headers: this.setToken()
      })
      .then(res => {
          // console.log(res.data)
          this.reviews = res.data
      })
    }
  }
</script>

<style>

</style>