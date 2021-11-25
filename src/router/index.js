import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import Community from '@/views/community/Community'
import Article from '@/views/community/Article'
import ArticleCreate from '@/views/community/ArticleCreate'
import ArticleUpdate from '@/views/community/ArticleUpdate'
import Home from '@/views/home/Home'
import ReviewsIndex from '@/views/reviews/ReviewIndex'


Vue.use(VueRouter)

const routes = [
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/profile/:username/',
    name: 'Profile',
    component: Profile,
  },  
  {
    path: '/community/community',
    name: 'Community',
    component: Community,
  },
  {
    path: '/community/article/:articleNum',
    name: 'Article',
    component: Article,
    
  },
  {
    path:'/community/articlecreate',
    name:'ArticleCreate',
    component:ArticleCreate,
  },
  {
    path: '/community/articleupdate/:articleNum',
    name: 'ArticleUpdate',
    component: ArticleUpdate,
    props:true,
    
  },
  {
    path:'/home',
    name:'Home',
    component:Home
  },
  {
    path: '/reviews/index',
    name: 'ReviewIndex',
    component: ReviewsIndex
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
