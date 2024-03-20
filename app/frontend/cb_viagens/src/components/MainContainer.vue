<template>
    <div class="main-container">
                    <div class="header">
                        <h1>Calculadora de Viagem</h1>
                    </div>
                    <div class="content">
                        <!-- Conteúdo aqui -->
                    </div>
    </div>
</template>
  
  <script>
  export default {
    name: 'MainContainer',
    props: {
      msg: String
    }
  }
  </script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
  <style scoped>
      .main-container {
            height: 70vh; /* Definir altura total da viewport */
            display: flex;
            flex-direction: column;
        }

        .header {
            background-color: black;
            color: white;
            text-align: center;
            padding: 20px 0;
            flex: 0 0 20%; /* 20% da altura total */
        }

        .content {
            background-color: white;
            flex: 1; /* O restante da altura total */
            padding: 20px;
        }
  </style>