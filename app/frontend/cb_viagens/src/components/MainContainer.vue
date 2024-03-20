<template>
    <div class="main-container">
        <div class="header">
            <h3>Calculadora de Viagem</h3>
        </div>
        <div class="content">
            <FormCalculator />
            <ResponseContainer class="response"/>
        </div>
    </div>
</template>
  
  <script>

  import FormCalculator from './FormCalculator.vue';
  import ResponseContainer from './ResponseContainer.vue'

  export default {
    name: 'MainContainer',
    props: {
      msg: String
    },
    components: {
        FormCalculator,
        ResponseContainer
    },
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
      .main-container {
            height: 80dvh; /* Definir altura total da viewport */
            width: 75dvw;
            display: flex;
            flex-direction: column;
            border-radius: 5px;
            margin: 5dvh;
        }

        .header {
            background-color: black;
            border-top-left-radius: 5px;
            border-top-right-radius: 5px;
            color: white;
            padding: 10px 20px;
            flex: 0 0 5%; /* 20% da altura total */
        }

        .header h3 {
            font-size: 1em;
            font-weight: bold;
        }

        .content {
            background-color: white;
            flex: 1; /* O restante da altura total */
            padding: 20px;
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: space-around;
        }

  </style>