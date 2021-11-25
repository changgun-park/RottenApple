<template>
  <div>
    <v-container fluid>
      <v-sheet 
          class="mt-5 mx-auto"
          max-width="100%"
          outline
          
      >
        <v-slide-group  show-arrows center-active>
          <movie-card v-for="movieCard in movieCards" :key="movieCard.id" :movieCard="movieCard">

              
          </movie-card>
        </v-slide-group>
      </v-sheet>
    </v-container>
    
  </div>

  <!-- <div>
    <movie-card
      v-for="movieCard in movieCards"
      :key="movieCard.id"
      :movieCard="movieCard"
    ></movie-card>
  </div> -->
</template>

<script>
import { mapState } from 'vuex'
import MovieCard from '@/components/MovieCard'
export default {
  name:'Home',
  components: {
    MovieCard  
  },

  computed:{
    ...mapState(['movieCards','is'])
  },
  created: function () {
    
    this.$store.dispatch('LoadMovieCards')
    this.$store.dispatch('LoadgenreCards')
  },
  Mount:function(){
    
  }
}
</script>

<style>

</style>