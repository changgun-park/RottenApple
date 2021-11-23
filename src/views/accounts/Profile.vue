<template>
  <div>
    <h1>{{ username }}의 Profile</h1>
    <span v-for="(genre, index) in genres" :key="`genre-${index}`">#{{ genre }}</span>
    <p v-if="is_expert">전문가!</p>
    <user-follow v-if="isNotMe" @refresh="refreshFollowCount"></user-follow>
    팔로워 수: {{ followers }}

    <!-- 작성 게시물, 좋아요한 영화는 링크걸기.. -->
    <div>
      <h2> 작성 게시물</h2>
      <ul>
        <li v-for="(article, index) in post_articles" :key="`article-${index}`">
          {{ article.title }} - {{ article.content }}
        </li>
      </ul>
    </div>
    <div>
      <h2> 좋아요한 영화</h2>
      <ul>
        <li v-for="(movie, index) in like_movies" :key="`movie-${index}`">
          {{ movie.title }} - {{ movie.overview }}
        </li>
      </ul>      
    </div>
    
  </div>
</template>

<script>
import axios from 'axios'
import UserFollow from '@/components/UserFollow'

export default {
  name: 'Profile',
  components: {
    UserFollow,
  },
  data: function() {
    return {
      isNotMe: null,
      username: null,
      genres: null,
      is_expert: false,
      post_articles: null,
      like_movies: null,
      followers: null,
    }
  },
  methods: {
    setToken:function(){
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    refreshFollowCount: function(data) {
      this.followers = data
    }
  },
  created: function () {
    // user 정보 받아오기
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/accounts/profile/${this.$route.params.username}/`,
      headers: this.setToken()
    })
    .then(res => {
      console.log(res)
      this.username = res.data.username
      this.genres = res.data.genres
      this.is_expert = res.data.is_expert
      this.post_articles = res.data.post_articles
      this.like_movies = res.data.like_movies
      this.followers = res.data.followers.length
    })
    const loggedUser = this.$store.state.loginUser
    const targetUser = this.$route.params.username

    if (loggedUser === targetUser){
      this.isNotMe = false
    } else {
      this.isNotMe = true
    }
  }
}
</script>

<style>

</style>