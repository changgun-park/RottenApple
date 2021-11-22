<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
      clipped
    >
      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
        app
        clipped-left
        color="indigo"
        dark
      >
        <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
  
        <v-toolbar-title>MovieGram</v-toolbar-title>
  
        <v-spacer></v-spacer>
        
        <v-btn text>Home</v-btn>
        <v-btn text>Reviews</v-btn>
        <v-btn text>Community</v-btn>
        
        <v-spacer></v-spacer>
  
        <v-menu offset-y
          left
          bottom
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              Text
              v-bind="attrs"
              v-on="on"
              color="indigo"
            >
              <v-icon>mdi-account</v-icon>Anonymous
              <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
          </template>
  
          <v-list>
            <v-list-item :to="{ name: 'Login' }">
              <v-list-item-title>Login</v-list-item-title>
            </v-list-item>
            <v-list-item :to="{ name: 'Signup' }">
              <v-list-item-title>Signup</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Profile</v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title>Logout</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
      
    <v-footer app>
      <span>2021</span>
    </v-footer>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'

  export default {
    components: { 
      // HelloWorld 
    },
    props: {
      source: String
    },
    data: function () {
      return {
        drawer: null,
        items: [
          { title: 'Dashboard', icon: 'mdi-view-dashboard' },
          { title: 'Photos', icon: 'mdi-image' },
          { title: 'About', icon: 'mdi-help-box' },
        ]
      } 
    }  
  }
</script>