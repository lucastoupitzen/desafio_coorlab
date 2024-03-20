<template>

    <div class="container">
        
        <div>
            <p>Nenhum dado selecionado</p>
        </div>

    </div>

</template>

<script>
  export default {
    name: 'ResponseContainer',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
      .container {
        width: fit-content;
        height: fit-content;
      }
  </style>