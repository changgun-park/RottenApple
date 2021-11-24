<template>



  <div>

    <v-app>
      <v-container>
          <v-sheet 
              class="mt-5 mx-auto"
              elevation="8"
              max-width="80%"
          >
              <v-slide-group mobile-break-point="1000" show-arrows center-active>
                  <movie-card v-for="movieCard in movieCards" :key="movieCard.id" :movieCard="movieCard">

                      
                  </movie-card>
              </v-slide-group>
          </v-sheet>
      </v-container>
    </v-app>
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
    ...mapState(['movieCards'])
  }
}
</script>

<style>

</style>