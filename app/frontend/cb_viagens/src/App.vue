<template>
    <body>
      <SideBar />
      <div class="content-size">
        <MainHeader />
        <MainContainer />
      </div>
      <AlertMessage v-if="$store.state.showAlert"/>
    </body>
</template>

<script>

import SideBar from './components/SideBar.vue';
import MainHeader from './components/MainHeader.vue';
import MainContainer from './components/MainContainer.vue';
import AlertMessage from './components/AlertMessage.vue'
import store from './store'   

export default {
  name: 'App',
  components: {
    SideBar,
    MainHeader,
    MainContainer,
    AlertMessage,
  }, 
  setup() {
    return {
      AlertMessage
    }
  },
}
</script>

<style>
  body {
    display: flex;
    flex-direction: row;
  }
  .content-size {
    display: flex;
    flex-direction: column;
  }
</style>
