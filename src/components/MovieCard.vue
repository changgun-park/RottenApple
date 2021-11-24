<template>
  <!-- <div>
    
    <v-card
      max-width="200"
      class="mx-auto"
    >
    
      <v-img
        :src="imgUrl"
        height="300px"
        dark
      >
        <v-row class="fill-height">
      
          <v-card-title class="white--text mx-auto pt-12">
            <div class="text-h4 mx-auto pt-12">
              Ali Conners
            </div>
          </v-card-title>
        </v-row>
      </v-img>
    </v-card>
   
  
</div> -->
  <div>
    
    <v-card width="200" class="ma-4">
        <v-card-title>
            <v-img height="200px" contain :src="imgUrl"></v-img>
        </v-card-title>
        <v-card-text>
            <b>€</b>
        </v-card-text>
    </v-card>
  </div>

</template>

<script>
export default {
  name:'MovieCard',
  props:{
    movieCard:Object
  },
  data:function(){
    return {
      imgUrl: `https://image.tmdb.org/t/p/w200${this.movieCard.poster_path}`
    }
  }
}
</script>

<style>

</style>