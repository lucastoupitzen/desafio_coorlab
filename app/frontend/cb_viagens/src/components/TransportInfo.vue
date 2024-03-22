<template>
    <div class="container">
      <div class="icon-area">
        <i :class="iconClass"></i>
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
      <div class="info-price">
        <div class="col">
          <div class="row">
            <p class="fw-bold">Preço</p>
          </div>
          <div class="row">
            <p>{{ campo4 }}</p>
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
      campo3: String,
      campo4: String,
      icon: String
    },
    computed: {
    // Calcula a classe do ícone com base no nome recebido como propriedade
    iconClass() {
      return `bi bi-${this.icon}`;
    }
  },
  }
  </script>
  
  <style scoped>
  .container {
    display: flex;
    flex-direction: row;
  }
  .icon-area {
    width: 80px;
    height: 80px;
    background-color: #04a8b5;
    border-bottom-left-radius: 5px;
    border-top-left-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .info-area {
    width: 240px;
    height: 80px;
    background-color: rgba(211, 211, 211, 0.554);
    border-bottom-right-radius: 5px;
    border-top-right-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center
  }
  .info-price {
    margin-left: 20px;
    width: 150px;
    height: 80px;
    background-color: rgba(211, 211, 211, 0.554);
    border-radius: 5px;
    display: flex;
    justify-content: center;
    align-items: center
  }
  .col {
    padding-left: 20px;
  }
  .row p{
    padding: 0;
    margin: 0;
  }
  .bi {
    color: white;
    font-size: 2em;
    font-weight: bold;
  }
  </style>
  