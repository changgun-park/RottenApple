<template>
  <div>
    <h1>회원가입</h1>
    <div>
      <label for="username">사용자 이름: </label>
      <input
      type="text" 
      id="username" 
      v-model="credentials.username"
      >
    </div>
    <div>
      <label for="password">비밀번호: </label>
      <input 
        type="password" 
        id="password"
        v-model="credentials.password"
      >
    </div>
    <div>
      <label for="passwordConfirmation">비밀번호 확인: </label>
      <input 
        type="password" 
        id="passwordConfirmation"
        v-model="credentials.passwordConfirmation"
        @keyup.enter="signup"
      >
    </div>
      
        <multiselect
          v-model="credentials.selected"
          :options="options"
          :multiple="true"
          :close-on-select="false"
          :clear-on-select="false"
          :preserve-search="true"
          track-by="id"
          label="name"
          :max="3"
          placeholder="">
            <span slot="maxElements">최대 3개만 선택 할 수 있습니다.</span>
        </multiselect>
    <button @click="signup">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'
import Multiselect from 'vue-multiselect'

export default {
  components: {
    Multiselect,
  },
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
        selected: []
      },
      alert: 'maxed out',
      options: [
        { id: 12, name: '모험',  },
        { id: 14, name: '판타지',  },
        { id: 16, name: '애니메이션',  },
        { id: 18, name: '드라마',  },
        { id: 27, name: '공포',  },
        { id: 28, name: '액션',  },
        { id: 35, name: '코미디'},
        { id: 36, name: '역사'},
        { id: 37, name: '서부'},
        { id: 53, name: '스릴러'},
        { id: 80, name: '범죄'},
        { id: 99, name: '다큐멘터리'},
        { id: 878, name: 'SF'},
        { id: 9648, name: '미스터리'},
        { id: 10402, name: '음악'},
        { id: 10749, name: '로맨스'},
        { id: 10751, name: '가족'},
        { id: 10752, name: '전쟁'},
        { id: 10770, name: 'TV영화'},
      ]
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(() => {
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>
<style>

</style>