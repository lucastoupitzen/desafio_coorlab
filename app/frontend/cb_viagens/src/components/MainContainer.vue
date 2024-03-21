<template>
    <div class="main-container">
      <div class="header custom-bg-color text-white p-2 ">
        <i class="bi bi-truck text-white"></i>
        <h3 class="m-0 title">Calculadora de Viagem</h3>
      </div>
      <div class="content p-4">
        <div class="form-calculator">
        <FormCalculator @transport-finded="changeResponse" />
      </div>
      <div class="response-container">
        <ResponseContainer class="response" />
      </div>
      </div>
    </div>
  </template>
  
  <script>
  import FormCalculator from './FormCalculator.vue';
  import ResponseContainer from './ResponseContainer.vue';
  
  export default {
    name: 'MainContainer',
    props: {
      msg: String
    },
    components: {
      FormCalculator,
      ResponseContainer
    },
  };
  </script>
  
  <style scoped>
  .main-container {
    height: 80vh; /* Definir altura total da viewport */
    width: 75vw;
    border-radius: 5px;
    margin: 5vh;
    margin-bottom: 0;
    position: relative;
  }
  
  .header{
    
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    display: flex;
    align-items: center;
  }

  .custom-bg-color{
    background-color:#2a3a59;
  }
  
  .header h3 {
    font-size: 1em;
    font-weight: bold;
  }
  
  .content {
    display: grid; /* Define o content como um grid container */
    grid-template-columns: 40% 60%; /* Divide o content em duas colunas com proporções de 40% e 60% */
    align-items: center;
}
  .form-calculator {
  padding-right: 10px; /* Adiciona um espaçamento à direita para separar o FormCalculator do ResponseContainer */
}

.response-container {
  padding-left: 10px; /* Adiciona um espaçamento à esquerda para separar o ResponseContainer do FormCalculator */
}
  .bi-truck {
    font-size: 1.5rem;
    margin-right: 1dvw;
    margin-left: 2dvw;
  }

  </style>