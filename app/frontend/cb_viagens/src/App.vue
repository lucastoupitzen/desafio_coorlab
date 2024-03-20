<template>
    <body>
      <SideBar />
      <div class="content-size">
        <MainHeader />
        <MainContainer />
      </div>
    </body>
</template>

<script>
import SideBar from './components/SideBar.vue';
import MainHeader from './components/MainHeader.vue';
import MainContainer from './components/MainContainer.vue';


export default {
  name: 'App',
  components: {
    SideBar,
    MainHeader,
    MainContainer,
  }
}
</script>

<style>
  body {
    display: flex;
    flex-direction: row;
  }
  .content-size {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
  }
</style>
