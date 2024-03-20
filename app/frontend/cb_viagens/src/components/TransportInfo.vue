<template>
    <div class="container">
      <div class="icon-area">
        <i class="fas fa-icon"></i>
      </div>
      <div class="info-area">
        <div class="col">
          <div class="row">
            <p class="fw-bold">{{ campo1 }}</p>
          </div>
          <div class="row">
            <p>{{ campo2 }}</p>
          </div>
          <div class="row">
            <p>{{ campo3 }}</p>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'TransportInfo',
    props: {
      campo1: String,
      campo2: String,
      campo3: String
    }
  }
  </script>
  
  <style scoped>
  .container {
    width: 23dvw; /* Largura do container */
    height: 15dvh; /* Altura do container */
    padding: 0;
    display: flex;
  }
  .icon-area {
    width: 25%;
    height: 100%;
    background-color: lightskyblue;
    border-bottom-left-radius: 5px;
    border-top-left-radius: 5px;
  }
  .info-area {
    width: 75%;
    height: 100%;
    background-color: lightgray;
    border-bottom-right-radius: 5px;
    border-top-right-radius: 5px;
  }
  .col {
    padding-left: 20px;
  }
  .row p{
    padding: 0;
    margin: 0;
  }
  </style>
  