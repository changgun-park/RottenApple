<template>
  <div>
    <v-container class="grey lighten-5 mt-10">
      <!-- Stack the columns on mobile by making one full-width and the other half-width -->
      <v-row>
        <v-col cols="8">
          
            <h2>{{ title }}</h2>
              <v-rating
              :value="4.5"
              class="d-inline"
              color="amber"
              dense
              half-increments
              readonly
              size="20"
            ></v-rating>
            <v-btn
              class="ma-2 d-inline"
              color="primary"
              dark
            >
              Expert
              <v-icon
                dark
                right
              >
                mdi-checkbox-marked-circle
              </v-icon>
            </v-btn>
            
            <span id="username" class="font-weight-medium">{{ user }} | {{ created_at }}</span> 
        </v-col>
        
      </v-row>
      <v-row align="start" justify="center">
        <v-col cols="12">
          <v-card class="pa-2">
            <v-card-title>
            {{ content }}
            </v-card-title>
            
          </v-card>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8">
          <!-- comment component -->
          <comment :reviewId="$route.params.reviewId"></comment>
        </v-col>
        <v-col cols="4">
          <v-card class="pa-2">
            movie card comes here
            <br>
            <br>
            <br>
            <br>
            <br>
          </v-card>
        </v-col>
        </v-row>
    </v-container>    
  </div>
</template>

<script>
import axios from 'axios'
import Comment from '@/components/Comment'

export default {
  components: {
    Comment,
  },
  name: 'ReviewDetail',
  data: function () {
    return {
      content: null,
      created_at: null,
      movie: null,
      rank: null,
      title: null,
      user: null,
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
  },
  created: function () {
    // Review 정보 가져오기
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/reviews/detail/${this.$route.params.reviewId}`,
      headers: this.setToken()
    })
      .then(res => {
      console.log(res.data)
      this.content = res.data.content
      this.created_at = res.data.created_at
      this.movie = res.data.movie
      this.rank = res.data.rank
      this.title = res.data.title
      this.user = res.data.user
    })
  },
}
</script>

<style>
  #username {
    font-size: 1.3rem;
  }
</style>