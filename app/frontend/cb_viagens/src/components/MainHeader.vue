<template>
    <header class="empty-header">

    </header>
  </template>
  
  <script>
  export default {
    name: 'MainHeader',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
      .empty-header{
        height: 13dvh;
        width: auto;
        border-bottom: 3px solid rgba(128, 128, 128, 0.593);
      }
  </style>